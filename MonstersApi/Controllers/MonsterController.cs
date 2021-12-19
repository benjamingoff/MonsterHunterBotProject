using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using MonstersApi.Services;
using System.Threading.Tasks;

namespace MonstersApi.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class MonsterController : Controller
    {
        private readonly IMonsterService _monsterService;

        public MonsterController(IMonsterService monsterService)
        {
            _monsterService = monsterService;
        }

        // GET: MonsterController/Details/5
        [HttpGet]
        [Route("/{name}")]
        public async Task<IActionResult> GetMonsterByName(string name)
        {
            var monster = await _monsterService.GetMonsterByNameAsync(name);
            if (monster == null)
            {
                return NotFound();
            }
            return Ok(monster);
        }
    }
}
