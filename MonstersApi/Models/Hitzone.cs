namespace MonstersApi.Models
{
    public class Hitzone
    {
        public string Name { get; set; }

        public HitzoneData DamageValues { get; set; }

        public ElementData ElementValues { get; set; }

        public AilmentData AilmentValues { get; set; }

        public Hitzone(string Name, HitzoneData DamageValues, ElementData ElementValues, AilmentData AilmentValues)
        {
            this.Name = Name;
            this.DamageValues = DamageValues;
            this.ElementValues = ElementValues;
            this.AilmentValues = AilmentValues;
        }
    }
}
