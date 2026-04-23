"""
DCS Dynamic Campaign -- Moteur de campagne dynamique pour DCS World.
Genere et suit des missions en fonction de l'etat du front.
"""

import json
import random
from dataclasses import dataclass, field
from typing import List


MISSION_TYPES = ["STRIKE", "CAP", "CAS", "SEAD", "RECON"]
WEATHER_CONDITIONS = ["Clear", "Scattered clouds", "Overcast", "Fog", "Rain"]
AIRCRAFT = {
    "STRIKE": ["F/A-18C", "F-16C", "Su-25T"],
    "CAP":    ["F-15C", "MiG-29A", "F/A-18C"],
    "CAS":    ["A-10C", "Su-25T", "AH-64D"],
    "SEAD":   ["F-16C", "Su-27"],
    "RECON":  ["F/A-18C", "MiG-21"],
}


@dataclass
class Mission:
    id: int
    type: str
    target: str
    aircraft: str
    weather: str
    threat_level: str   # LOW / MEDIUM / HIGH
    status: str = "PLANNED"

    def __str__(self):
        return (
            f"[M{self.id:03d}] {self.type:<8}  Target: {self.target:<20} "
            f"Aircraft: {self.aircraft:<12}  Weather: {self.weather:<18} "
            f"Threat: {self.threat_level:<6}  Status: {self.status}"
        )


@dataclass
class Campaign:
    theater: str
    name: str
    day: int = 1
    blue_score: int = 50
    red_score: int = 50
    missions: List[Mission] = field(default_factory=list)
    _next_id: int = field(default=1, repr=False)

    def generate_mission(self) -> Mission:
        """Genere une nouvelle mission en fonction de l'etat du front."""
        from theaters import THEATERS
        theater_data = THEATERS.get(self.theater, THEATERS["Caucasus"])
        targets = theater_data["targets"]
        mission_type = random.choice(MISSION_TYPES)
        target = random.choice(targets)
        aircraft = random.choice(AIRCRAFT[mission_type])
        weather = random.choice(WEATHER_CONDITIONS)
        threat = random.choice(["LOW", "LOW", "MEDIUM", "MEDIUM", "HIGH"])
        m = Mission(id=self._next_id, type=mission_type, target=target,
                    aircraft=aircraft, weather=weather, threat_level=threat)
        self.missions.append(m)
        self._next_id += 1
        return m

    def complete_mission(self, mission_id: int, success: bool):
        """Marque une mission comme terminee et met a jour les scores."""
        for m in self.missions:
            if m.id == mission_id:
                m.status = "SUCCESS" if success else "FAILED"
                if success:
                    self.blue_score = min(100, self.blue_score + random.randint(3, 8))
                    self.red_score = max(0, self.red_score - random.randint(2, 6))
                else:
                    self.red_score = min(100, self.red_score + random.randint(2, 5))
                break

    def next_day(self):
        """Passe au jour suivant."""
        self.day += 1
        self.red_score = max(0, self.red_score - random.randint(0, 3))
        self.blue_score = min(100, self.blue_score + random.randint(0, 2))
        print(f"\n--- Jour {self.day} | Blue : {self.blue_score}% | Red : {self.red_score}% ---")

    def status_report(self):
        total = len(self.missions)
        done = sum(1 for m in self.missions if m.status in ("SUCCESS", "FAILED"))
        success = sum(1 for m in self.missions if m.status == "SUCCESS")
        print(f"\n=== RAPPORT DE CAMPAGNE -- {self.name} ({self.theater}) ===")
        print(f"  Jour actuel : {self.day}")
        print(f"  Score Blue  : {self.blue_score}%")
        print(f"  Score Red   : {self.red_score}%")
        print(f"  Missions    : {total} total  |  {done} terminees  |  {success} reussies\n")
        for m in self.missions:
            print(f"  {m}")

    def save(self, path: str):
        data = {"theater": self.theater, "name": self.name, "day": self.day,
                "blue_score": self.blue_score, "red_score": self.red_score,
                "missions": [vars(m) for m in self.missions]}
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Campagne sauvegardee : {path}")

    @classmethod
    def load(cls, path: str) -> "Campaign":
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        c = cls(theater=data["theater"], name=data["name"],
                day=data["day"], blue_score=data["blue_score"], red_score=data["red_score"])
        c.missions = [Mission(**m) for m in data["missions"]]
        c._next_id = max((m.id for m in c.missions), default=0) + 1
        return c


if __name__ == "__main__":
    camp = Campaign(theater="Caucasus", name="Operation Koba")
    print(f"Campagne : {camp.name} | Theatre : {camp.theater}\n")
    for _ in range(4):
        m = camp.generate_mission()
        print(f"Mission generee : {m}")
    camp.complete_mission(1, success=True)
    camp.complete_mission(2, success=False)
    camp.complete_mission(3, success=True)
    camp.next_day()
    camp.generate_mission()
    camp.complete_mission(5, success=True)
    camp.status_report()
    camp.save("save_koba.json")
