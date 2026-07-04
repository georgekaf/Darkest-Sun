
Psionicist `Improved`
```
// Psionicist `Improved`

const EFFECT_NAME = "Improve";
const FLAG_SCOPE = "world";
const FLAG_KEY = "shadowdarkImproveLevelBonus";

function getActorLevel(actor) {
  return Number(foundry.utils.getProperty(actor, "system.level.value") ?? 0) || 0;
}

function actorHasImprove(actor) {
  return Array.from(actor.effects ?? []).some(e =>
    !e.disabled &&
    (
      e.name === EFFECT_NAME ||
      e.getFlag(FLAG_SCOPE, FLAG_KEY) === true
    )
  );
}

if (!globalThis.__shadowdarkImproveLevelHookInstalled) {
  Hooks.on("SD-Stat-Check", async (config) => {
    const actor = config.actorUuid ? await fromUuid(config.actorUuid) : null;
    if (!actor) return true;
    if (!actorHasImprove(actor)) return true;

    const level = getActorLevel(actor);
    if (!level) return true;

    if (config.__improveLevelApplied) return true;
    config.__improveLevelApplied = true;

    const roll = config.mainRoll;
    if (!roll) return true;

    roll.formula = `${roll.formula}+${level}`;

    roll.tooltips = [
      roll.tooltips,
      `Improve: +${level} to ability check`
    ].filter(Boolean).join(", ");

    return true;
  });

  globalThis.__shadowdarkImproveLevelHookInstalled = true;
  console.log("Improve level hook installed.");
}

const actors = canvas.tokens.controlled
  .map(t => t.actor)
  .filter(Boolean);

if (!actors.length) {
  ui.notifications.info("Improve hook installed. Select a token and run again to toggle Improve.");
  return;
}

for (const actor of actors) {
  const existing = actor.effects.find(e =>
    e.name === EFFECT_NAME ||
    e.getFlag(FLAG_SCOPE, FLAG_KEY) === true
  );

  if (existing) {
    await existing.delete();
    ui.notifications.info(`${actor.name}: Improve removed.`);
    continue;
  }

  const level = getActorLevel(actor);

  await actor.createEmbeddedDocuments("ActiveEffect", [{
    name: EFFECT_NAME,
    img: "icons/magic/control/buff-strength-muscle-damage-red.webp",
    disabled: false,
    transfer: false,
    flags: {
      [FLAG_SCOPE]: {
        [FLAG_KEY]: true
      }
    },
    changes: [
      {
        key: "system.bonuses.meleeAttackBonus",
        mode: CONST.ACTIVE_EFFECT_MODES.ADD,
        value: String(level),
        priority: 20
      },
      {
        key: "system.bonuses.rangedAttackBonus",
        mode: CONST.ACTIVE_EFFECT_MODES.ADD,
        value: String(level),
        priority: 20
      }
    ]
  }]);

  ui.notifications.info(`${actor.name}: Improve applied. +${level} attacks and ability checks.`);
}
```

Apply Defensive Flurry
```
// Defensive Flurry

const EFFECT_NAME = "Defensive Flurry";
const FLAG_SCOPE = "world";
const FLAG_KEY = "shadowdarkDefensiveFlurryAC";

const AC_PATH = "system.attributes.ac.value";

// Change this if your attack bonus is somewhere else
const ATTACK_BONUS_PATH = "system.bonuses.meleeAttackBonus";

function getAttackBonus(actor) {
  return Number(foundry.utils.getProperty(actor, ATTACK_BONUS_PATH) ?? 0) || 0;
}

const token = canvas.tokens.controlled[0];

if (!token?.actor) {
  ui.notifications.warn("Select one token first.");
  return;
}

const actor = token.actor;

// Remove previous Defensive Flurry effect if it exists
const existing = Array.from(actor.effects ?? []).find(e =>
  e.name === EFFECT_NAME ||
  e.getFlag(FLAG_SCOPE, FLAG_KEY) === true
);

if (existing) {
  await existing.delete();
}

const attackBonus = getAttackBonus(actor);
const formula = `1d20 + ${attackBonus}`;

const roll = await new Roll(formula).evaluate({ async: true });

await roll.toMessage({
  speaker: ChatMessage.getSpeaker({ actor, token }),
  flavor: `${actor.name} uses Defensive Flurry. Attack roll total becomes AC for 1 round.`
});

const newAC = roll.total;

const combat = game.combat;
const isInCombat = combat && combat.combatants.some(c => c.tokenId === token.id);

const duration = isInCombat
  ? {
      rounds: 1,
      startRound: combat.round,
      startTurn: combat.turn
    }
  : {
      seconds: 60,
      startTime: game.time.worldTime
    };

await actor.createEmbeddedDocuments("ActiveEffect", [{
  name: EFFECT_NAME,
  img: "icons/skills/melee/sword-damaged-broken-glow-red.webp",
  disabled: false,
  transfer: false,
  duration,
  flags: {
    [FLAG_SCOPE]: {
      [FLAG_KEY]: true
    }
  },
  changes: [
    {
      key: AC_PATH,
      mode: CONST.ACTIVE_EFFECT_MODES.OVERRIDE,
      value: String(newAC),
      priority: 50
    }
  ]
}]);

ui.notifications.info(`${actor.name}: AC is now ${newAC} for 1 round.`);
```

Reset `Defensive Flurry`

```
// Reset Defensive Flurry

const EFFECT_NAME = "Defensive Flurry";
const FLAG_SCOPE = "world";
const FLAG_KEY = "shadowdarkDefensiveFlurryAC";

const actors = canvas.tokens.controlled
  .map(t => t.actor)
  .filter(Boolean);

if (!actors.length) {
  ui.notifications.warn("Select at least one token.");
  return;
}

for (const actor of actors) {
  const effects = Array.from(actor.effects ?? []).filter(e =>
    e.name === EFFECT_NAME ||
    e.getFlag(FLAG_SCOPE, FLAG_KEY) === true
  );

  if (!effects.length) {
    ui.notifications.info(`${actor.name}: No Defensive Flurry effect found.`);
    continue;
  }

  await actor.deleteEmbeddedDocuments(
    "ActiveEffect",
    effects.map(e => e.id)
  );

  ui.notifications.info(`${actor.name}: Defensive Flurry removed. AC restored.`);
}
```