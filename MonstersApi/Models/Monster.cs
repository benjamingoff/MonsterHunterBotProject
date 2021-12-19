using MongoDB.Bson.Serialization.Attributes;
using System.Collections.Generic;

namespace MonstersApi.Models
{
    public class Monster
    {
        // TODO: Implement classes that will allow the JSON to be read into the model
        // Explanation I'm working off of: https://docs.microsoft.com/en-us/dotnet/standard/serialization/system-text-json-how-to?pivots=dotnet-6-0

        [BsonId]
        [BsonRepresentation(MongoDB.Bson.BsonType.ObjectId)]
        public string _id { get; set; }

        public string name { get; set; }

        public List<string> habitats { get; set; }

        public Dictionary<string, HitzoneData> hitzones { get; set; }

        public Dictionary<string, ElementData> elements { get; set; }

        public AilmentData ailments { get; set; }

        public Monster()
        {

        }
    }
}
