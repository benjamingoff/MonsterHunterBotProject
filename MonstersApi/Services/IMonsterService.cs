using MonstersApi.Models;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace MonstersApi.Services
{
    public interface IMonsterService
    {
        Task<Monster> GetMonsterByNameAsync(string name);
        Task<List<Monster>> GetAllMonstersAsync();
    }
}
