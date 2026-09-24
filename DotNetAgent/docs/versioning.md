# Versioning & Evolution Strategy

The Universal .NET AI Core Team adheres strictly to [Semantic Versioning 2.0.0](https://semver.org/).

---

## 1. Core Team Versioning (`VERSION`)

The file `VERSION` in the repository root defines the current release of the Core Team (e.g. `1.0.0`).

### Version Segments
- **MAJOR (`X.0.0`)**: Incompatible changes to core agent handoff protocols, removal of core agents, or breaking changes to rule precedence hierarchy.
- **MINOR (`1.X.0`)**: Addition of new core agents, new core skills, new non-breaking rules, or enhancements to project profiler detection.
- **PATCH (`1.0.X`)**: Bug fixes in skills, rule clarification, documentation updates, or test fixture enhancements.

---

## 2. Independent Technology Pack Evolution

Future Technology Packs will evolve independently from the Core Team to support rapidly changing framework releases without destabilizing core orchestration:

```text
Universal .NET Core Team: v1.0.x
  ├── Technology Pack: modern-dotnet (v10.x / v9.x / v8.x)
  ├── Technology Pack: aspnet-core (v10.x / v9.x / v8.x)
  ├── Technology Pack: ef-core (v10.x / v9.x / v8.x)
  ├── Technology Pack: abp-framework (v9.x / v8.x / v7.x)
  └── Technology Pack: legacy-dotnet-framework (v4.8.x / v4.7.x)
```

This decoupled versioning allows developers on ABP 8 or EF Core 9 to pin specific Technology Pack versions while continuing to receive updates to the Universal Core Team.
