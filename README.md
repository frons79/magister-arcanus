# Magister Arcanus

Discord bot for RPG random tables.

## Permissions: Demiurgo

Magister Arcanus does **not** bind authorization to the person who built the bot.
Each Discord server has its own unique **Demiurgo** permission.

- The permission is represented by the `Demiurgo` Discord role.
- Exactly one member may hold that role at a time.
- The first Demiurgo is appointed by a server administrator.
- After that, only the current Demiurgo can transfer the permission to another member.
- The bot's administrative commands are restricted to the current Demiurgo.
- Removing the Demiurgo role from a member revokes the permission.
- The bot never uses the GitHub account, application owner, or an environment variable to decide who may operate it.

The implementation creates the role automatically when the first Demiurgo is appointed. The bot must have the Discord permissions required to manage roles, and its role must be above the `Demiurgo` role in the server role hierarchy.
