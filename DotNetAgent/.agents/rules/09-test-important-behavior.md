# Rule 09: Test Important Behavior

## Rule Statement
Automated tests must focus on validating observable behavior, domain rules, edge cases, and contract stability. Do not author vacuous tests that verify trivial getters/setters or test mock framework internals.

## Why It Exists
High line-coverage with meaningless tests provides false confidence while burdening maintenance. Testing observable behavior ensures true regression protection.

## Good Example
```csharp
[Fact]
public async Task TransferFunds_WhenBalanceInsufficient_ReturnsFailureAndDoesNotDebit()
{
    var account = new Account(balance: 50m);
    var result = account.Withdraw(100m);
    
    result.IsFailure.Should().BeTrue();
    account.Balance.Should().Be(50m);
}
```

## Bad Example
```csharp
[Fact]
public void CustomerDto_NameProperty_SetsAndGets()
{
    var dto = new CustomerDto { Name = "John" };
    Assert.Equal("John", dto.Name); // Vacuous property test
}
```

## Exception Cases
None. Every authored test must protect a genuine business rule or functional requirement.

## Enforcement Guidance
The Test Engineer will review test suites to ensure assertions validate functional contracts and failure modes.
