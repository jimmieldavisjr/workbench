public static class InfrastructureExtensions
{
    public static IServiceCollection AddInfrastructure(this IServiceCollection services)
    {
        services.AddSingleton<IStripePaymentGateway, StripePaymentGateway>();
        services.AddSingleton<ISendGridEmailSender, SendGridEmailSender>(); 

        return services;
    }
}