using Volo.Abp.Modularity;
using Volo.Abp.Autofac;
using Volo.Abp.AspNetCore.Mvc;

namespace MyProject
{
    [DependsOn(
        typeof(AbpAspNetCoreMvcModule),
        typeof(AbpAutofacModule)
    )]
    public class MyProjectAppModule : AbpModule
    {
        public override void ConfigureServices(ServiceConfigurationContext context)
        {
            // Configure ABP modular services
        }
    }
}
