using System;

namespace MonstersApi.Models
{
    public class ElementData
    {
        public int Fire { get; set; }

        public int Water { get; set; }

        public int Thunder { get; set; }

        public int Ice { get; set; }

        public int Dragon { get; set; }

        public ElementData(string Fire, string Water, string Thunder, string Ice, string Dragon)
        {
            this.Fire = Int32.Parse(Fire);
            this.Water = Int32.Parse(Water);
            this.Thunder = Int32.Parse(Thunder);
            this.Ice = Int32.Parse(Ice);
            this.Dragon = Int32.Parse(Dragon);
        }
    }
}
