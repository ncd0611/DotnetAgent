# Rule 01: Evidence First

## Rule Statement
Never assume, guess, or hypothesize about technical stacks, bug causes, compiler errors, or performance bottlenecks without concrete repository evidence. Inspect actual metadata, compiler logs, diagnostic traces, or test outputs before formulating an approach.

## Why It Exists
AI models frequently hallucinate framework versions, imagine architecture patterns that do not exist in the codebase, or jump to speculative fixes that mask symptoms rather than addressing root causes. Demanding empirical evidence grounds all actions in reality.

## Good Example
```text
Inspected WebApi.csproj (line 7): Found <TargetFramework>net8.0</TargetFramework>.
Ran dotnet test: Discovered failure in OrderServiceTests.cs line 42 with NullReferenceException caused by missing Customer null-check in OrderService.cs line 88.
```

## Bad Example
```text
"The repository has a Controllers folder, so it must be ASP.NET Core 8 with EF Core. I'll add a CQRS handler to fix the bug."
```

## Exception Cases
None. Evidence must precede action in every scenario.

## Enforcement Guidance
The Tech Lead and Code Reviewer will reject any implementation proposal that lacks references to concrete files, line numbers, or diagnostic logs.
