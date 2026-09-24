---
name: test-pyramid
description: Guides task-driven test strategy selection across the testing pyramid (unit tests, integration tests, WebApplicationFactory API tests, E2E) based on change scope.
---

# Test Pyramid Strategy Skill

## 1. When to Use
- When planning test coverage for new features, bug fixes, or architectural changes.
- When determining whether a change requires unit tests, integration tests, or API tests.
- When configuring `WebApplicationFactory` in ASP.NET Core test projects.

## 2. When NOT to Use
- When writing pure documentation or profiling projects.

## 3. Test Granularity Matrix

| Layer | Target Under Test | Speed | Isolation | Best Used For |
| :--- | :--- | :--- | :--- | :--- |
| **Unit Tests** | Domain entities, pure algorithmic methods, value objects | Very Fast (<10ms) | Complete (In-memory, mocks) | Business calculations, domain invariants, edge cases |
| **Subsystem Tests** | Application use cases, command/query handlers | Fast (<50ms) | High (Mock external I/O) | Orchestration, validation logic, result mapping |
| **Integration Tests** | Data access, repositories, database queries | Moderate (<500ms) | Partial (Real DB or LocalDB) | SQL correctness, EF mappings, transaction rollbacks |
| **API Tests** | Full HTTP request/response pipeline (`WebApplicationFactory`) | Moderate (<1s) | Full in-memory web host | Authentication, routing, status codes, serialization |
| **E2E Tests** | Complete deployed system | Slow (>5s) | External dependencies | Critical customer workflows, payment gateways |

## 4. ASP.NET Core API Testing with WebApplicationFactory
```csharp
public class CustomerApiTests : IClassFixture<WebApplicationFactory<Program>>
{
    private readonly HttpClient _client;

    public CustomerApiTests(WebApplicationFactory<Program> factory)
    {
        _client = factory.CreateClient();
    }

    [Fact]
    public async Task GetCustomer_WithValidId_ReturnsOkAndCustomer()
    {
        var response = await _client.GetAsync("/api/customers/123");
        response.StatusCode.Should().Be(HttpStatusCode.OK);
        
        var customer = await response.Content.ReadFromJsonAsync<CustomerDto>();
        customer.Should().NotBeNull();
        customer!.Id.Should().Be(123);
    }
}
```

## 5. Anti-Patterns
- **Testing Mocks Instead of Behavior**: Setting up 40 lines of mock expectations to test a 2-line method that simply forwards a call.
- **Requiring E2E for Minor Fixes**: Insisting on running a full browser automation suite for a simple validation regex fix.

## 6. Verification Checklist
- [ ] Appropriate test level selected for the change.
- [ ] Tests execute deterministically without flaky dependencies.
- [ ] Assertions validate observable outcomes rather than mock internals.
