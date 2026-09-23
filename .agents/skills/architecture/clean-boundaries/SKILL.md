---
name: clean-boundaries
description: Enforces inward dependency direction, domain isolation, and interface abstraction across Clean Architecture, DDD, and N-Tier patterns.
---

# Clean Boundaries Skill

## 1. When to Use
- When introducing new services, handlers, entities, or infrastructure adapters.
- When evaluating layer violations, circular project dependencies, or leaky domain abstractions.
- When structuring modular monoliths, ABP modules, or Clean Architecture layers.

## 2. When NOT to Use
- In simple, single-project scripts or utility console apps.
- When modifying legacy systems where existing project structure is deliberately monolithic.

## 3. Workflow & Procedure
1. **Verify Dependency Direction**:
   - Confirm that inner layers have NO references to outer layers:
     - Domain $\rightarrow$ No dependencies on Application, Infrastructure, or Presentation.
     - Application $\rightarrow$ References only Domain; defines interfaces for Infrastructure.
     - Infrastructure $\rightarrow$ Implements Application/Domain interfaces; references EF Core, HTTP clients, message buses.
     - Presentation / API $\rightarrow$ Entry point; configures DI container and routes requests.
2. **Prevent Leaky Abstractions**:
   - Ensure EF Core entities, `DbContext`, or HTTP types (`HttpContext`, `HttpRequest`) do not leak into Domain entities.
   - Use Data Transfer Objects (DTOs) or domain view models across boundary lines.
3. **Keep Use Cases Focused**:
   - Single responsibility for each application use case / command handler.

## 4. Decision Guidance
- If a project uses classic 3-Tier (`Web -> BLL -> DAL`), respect that structure; do not artificially force Hexagonal or Clean Architecture boundaries.
- If a domain model requires persistence information, define a repository interface in Domain/Application and implement in Infrastructure.

## 5. Anti-Patterns
- **Direct Infrastructure Coupling**: Referencing `Microsoft.EntityFrameworkCore` inside the core Domain project.
- **Fat Controllers**: Placing SQL queries or business rules directly inside API controller methods.

## 6. Verification Checklist
- [ ] Inward dependency direction verified.
- [ ] No outer framework types in Domain layer.
- [ ] Contracts decoupled from concrete infrastructure adapters.
