using MonstersApi.Models;
using System.Threading.Tasks;

namespace MonstersApi.Services
{
    public interface IMonsterService
    {
        Task<Monster> GetMonsterByNameAsync(string name);
    }
}
