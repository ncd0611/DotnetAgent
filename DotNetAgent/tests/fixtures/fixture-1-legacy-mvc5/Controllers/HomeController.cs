using System;
using System.Web.Mvc;

namespace LegacyMvcApp.Controllers
{
    public class HomeController : Controller
    {
        public ActionResult Index()
        {
            ViewBag.Message = "Legacy MVC 5 Home Page";
            return View();
        }
    }
}
