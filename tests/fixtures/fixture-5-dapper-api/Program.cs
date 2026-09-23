using System.Data;
using Microsoft.Data.SqlClient;
using Dapper;

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddScoped<IDbConnection>(sp => new SqlConnection(builder.Configuration.GetConnectionString("Default")));

var app = builder.Build();

app.MapGet("/customers/{id:int}", async (int id, IDbConnection db) =>
{
    var customer = await db.QueryFirstOrDefaultAsync("SELECT Id, Name FROM Customers WHERE Id = @Id", new { Id = id });
    return customer is not null ? Results.Ok(customer) : Results.NotFound();
});

app.Run();
