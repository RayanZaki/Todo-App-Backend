from models.StatsModel import Statistics
from fastapi import Depends
from repositories.StatsRepository import StatsRepository



class StatsService:
    statsRepository: StatsRepository

    def __init__(
        self,
        statsRepository: StatsRepository = Depends(),
    ) -> None:
        self.statsRepository = statsRepository

    def get(self) -> Statistics:
        return self.statsRepository.get()

    def increment_todo_count(self):
        stats = self.get()
        stats.n_todos += 1
        print("updating")
        return self.statsRepository.update(stats)
    
    def increment_modified_count(self):
        stats = self.get()
        stats.n_modifications += 1
        stats.n_modified += 1
        return self.statsRepository.update(stats)
    
    def increment_deleted_count(self): 
        stats = self.get()
        stats.n_deleted += 1
        stats.n_todos -= 1
        return self.statsRepository.update(stats)
    
    def increment_modification_count(self):
        stats = self.get()
        stats.n_modifications += 1
        return self.statsRepository.update(stats)