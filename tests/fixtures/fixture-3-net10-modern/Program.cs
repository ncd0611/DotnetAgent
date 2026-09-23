var builder = WebApplication.CreateSlimBuilder(args);

var app = builder.Build();

app.MapGet("/", () => Results.Ok(new { Message = "Modern .NET 10 Slim API" }));

app.Run();
