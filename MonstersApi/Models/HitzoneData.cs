using System;

namespace MonstersApi.Models
{
    public class HitzoneData
    {
        public int Cutting { get; set; }

        public int Impact { get; set; } 

        public int Shot { get; set; }

        public HitzoneData(string Cutting, string Impact, string Shot)
        {
            this.Cutting = Int32.Parse(Cutting);
            this.Impact = Int32.Parse(Impact);
            this.Shot = Int32.Parse(Shot);
        }
    }
}
