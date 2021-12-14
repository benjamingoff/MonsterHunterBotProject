using MongoDB.Bson.Serialization.Attributes;
using System.Collections.Generic;

namespace MonstersApi.Models
{
    public class Monster
    {
        [BsonId]
        [BsonRepresentation(MongoDB.Bson.BsonType.ObjectId)]

        // TODO: Implement classes that will allow the JSON to be read into the model
        // Explanation I'm working off of: https://docs.microsoft.com/en-us/dotnet/standard/serialization/system-text-json-how-to?pivots=dotnet-6-0

        public string _id { get; set; }

        public string Name { get; set; }

        public List<string> Habitats { get; set; }

    }
}
