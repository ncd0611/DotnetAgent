# Rule 16: Legacy Safety Model (Maintenance $\ne$ Migration)

## Rule Statement
When operating in a legacy .NET Framework repository (such as .NET Framework 4.5–4.8, ASP.NET MVC 5, Web API 2, EF6, or WCF), agents are strictly forbidden from performing accidental modernization. Maintenance work must preserve existing frameworks, configuration files, and calling conventions.

## Why It Exists
Legacy enterprise systems have accumulated intricate production behaviors, IIS pipeline dependencies, and undocumented edge-case handlings. Speculative modernization (e.g. converting to async, removing `web.config`, replacing EF6 with EF Core) introduces catastrophic runtime deadlocks and pipeline failures.

## Prohibited Legacy Modernization Actions
Unless explicitly commanded by the user or strictly required for correctness:
1. **DO NOT** convert synchronous MVC 5 / Web API actions to `async/await` everywhere.
2. **DO NOT** upgrade the target framework from .NET Framework to modern .NET (.NET 8/10).
3. **DO NOT** delete or replace `web.config` with `appsettings.json`.
4. **DO NOT** replace `packages.config` with `<PackageReference>`.
5. **DO NOT** replace Entity Framework 6 with EF Core.
6. **DO NOT** replace WCF, ASMX, or OWIN with modern equivalents.
7. **DO NOT** introduce modern DI containers (Autofac, Microsoft.Extensions.DependencyInjection) if the project uses a custom ServiceLocator or manual instantiation.

## Good Example
```csharp
// In a legacy ASP.NET MVC 5 controller:
[HttpPost]
public ActionResult UpdateProfile(ProfileModel model)
{
    if (!ModelState.IsValid) return View(model);
    _legacyService.SaveProfile(model); // Preserving synchronous execution
    return RedirectToAction("Success");
}
```

## Bad Example
```csharp
// Agent unilaterally modernizes the action:
[HttpPost]
public async Task<ActionResult> UpdateProfile(ProfileModel model)
{
    // Calling an internal helper that uses .Result inside async action 
    // on legacy SynchronizationContext -> Immediate deadlock!
    await _legacyService.SaveProfileAsync(model);
}
```

## Exception Cases
When the user explicitly issues a modernization or migration mandate (in which case, route to `Migration Engineer`).

## Enforcement Guidance
The Tech Lead and Code Reviewer will immediately reject any PR modifying legacy projects that violates these safety boundaries.
