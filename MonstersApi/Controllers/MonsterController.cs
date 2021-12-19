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

        // GET: /api/MonsterName
        [HttpGet]
        [Route("/api/{name}")]
        public async Task<IActionResult> GetMonsterByName(string name)
        {
            var monster = await _monsterService.GetMonsterByNameAsync(name);
            if (monster == null)
            {
                return NotFound();
            }
            return Ok(monster);
        }

        // NOTE: This returns all of the monster objects (literally an entire database dump) --Very expensive to use
        [HttpGet]
        [Route("/api/GetAll")]
        public async Task<IActionResult> GetAllMonsterNames()
        {
            var monsters = await _monsterService.GetAllMonstersAsync();
            if (monsters == null)
            {
                return NotFound();
            }
            return Ok(monsters);
        }
    }
}
