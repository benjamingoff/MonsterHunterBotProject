using MongoDB.Bson.Serialization.Attributes;
using System.Collections.Generic;

namespace MonstersApi.Models
{
    public class Monster
    {

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
