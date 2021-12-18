namespace MonstersApi.Models
{
    public class AilmentData
    {
        public int Poisin { get; set; }
        public int Stun { get; set; }
        public int Paralysis { get; set; }
        public int Sleep { get; set; } 
        public int Blast { get; set; }
        public int Exhaust { get; set; }
        public int Fireblight { get; set; }
        public int Waterblight { get; set; }
        public int Thunderblight { get; set; }
        public int Iceblight { get; set; }

        public AilmentData(int Poisin, int Stun, int Paralysis, int Sleep, int Blast,
                            int Exhaust, int Fireblight, int Waterblight,
                            int Thunderblight, int Iceblight)
        {
            this.Poisin = Poisin;
            this.Stun = Stun;
            this.Paralysis = Paralysis;
            this.Sleep = Sleep;
            this.Blast = Blast;
            this.Exhaust = Exhaust;
            this.Fireblight = Fireblight;
            this.Waterblight = Waterblight;
            this.Thunderblight = Thunderblight;
            this.Iceblight = Iceblight;
        }
    }
}
