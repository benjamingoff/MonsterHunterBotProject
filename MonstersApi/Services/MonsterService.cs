using Microsoft.Extensions.Options;
using MongoDB.Driver;
using MonstersApi.Configuration;
using MonstersApi.Models;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace MonstersApi.Services
{
    public class MonsterService : IMonsterService
    {
        private readonly IMongoCollection<Monster> _monsters;
        private readonly MonsterConfiguration _settings;

        public MonsterService(IOptions<MonsterConfiguration> settings)
        {
            _settings = settings.Value;
            var client = new MongoClient(_settings.ConnectionString);
            var database = client.GetDatabase(_settings.DatabaseName);
            _monsters = database.GetCollection<Monster>(_settings.MonsterCollectionName);
        }

        public async Task<Monster> GetMonsterByNameAsync(string Name)
        {
            return await _monsters.Find<Monster>(c => c.name == Name).FirstOrDefaultAsync();
        }

        public async Task<List<Monster>> GetAllMonstersAsync()
        {
            return await _monsters.Find(c => true).ToListAsync();
        }
    }
}
