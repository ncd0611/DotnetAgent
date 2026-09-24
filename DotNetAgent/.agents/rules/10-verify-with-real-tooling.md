# Rule 10: Verify With Real Tooling

## Rule Statement
Never assume that written code compiles or that tests pass based on internal reasoning alone. Always invoke real compilers (`dotnet build`, `msbuild`) and real test runners (`dotnet test`) to verify changes before concluding a task.

## Why It Exists
LLMs can make subtle syntax errors (missing semicolons, incorrect generic arguments, namespace typos) that appear plausible but fail compilation. Real tooling provides ground truth.

## Good Example
```bash
# Executing real CLI tooling:
dotnet build --no-incremental -c Release
dotnet test --filter "FullyQualifiedName~CustomerServiceTests"
# Output analyzed and confirmed: 0 errors, 14 passed.
```

## Bad Example
```text
"I have added the endpoint and it looks completely correct and conforms to C# standards, so we are finished!" (Without running build or test tools).
```

## Exception Cases
When operating in an environment or offline sandbox where the .NET SDK or runtime tooling is not installed or available. In this case, the agent must explicitly disclose that tooling verification was skipped.

## Enforcement Guidance
The Tech Lead will not sign off on any implementation without attached execution logs from `dotnet build` or `dotnet test`.
