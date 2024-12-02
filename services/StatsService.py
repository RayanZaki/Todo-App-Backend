from models.StatsModel import Statistics
from fastapi import Depends
from repositories.StatsRepository import StatsRepository



class StatsService:
    statsRepository: StatsRepository

    def __init__(
        self,
        statsRepository: StatsRepository = Depends(),
    ) -> None:
        """
        Initializes the StatsService with a dependency-injected StatsRepository.
        """
        self.statsRepository = statsRepository

    def get(self) -> Statistics:
        """
        Retrieves the current statistical data from the repository.
        """
        return self.statsRepository.get()

    def increment_todo_count(self):
        """
        Increments the count of todos (`n_todos`) and total todos (`n_total_todos`) 
        in the statistics and updates the repository.
        """
        stats = self.get()
        stats.n_todos += 1
        stats.n_total_todos += 1
        print("updating")
        return self.statsRepository.update(stats)
    
    def increment_modified_count(self):
        """
        Increments the count of modifications (`n_modifications`) and 
        modified todos (`n_modified`) in the statistics and updates the repository.
        """
        stats = self.get()
        stats.n_modifications += 1
        stats.n_modified += 1
        return self.statsRepository.update(stats)
    
    def increment_deleted_count(self):
        """
        Increments the count of deleted todos (`n_deleted`) and decrements
        the count of current todos (`n_todos`) in the statistics and updates the repository.
        """ 
        stats = self.get()
        stats.n_deleted += 1
        stats.n_todos -= 1
        return self.statsRepository.update(stats)
    
    def increment_modification_count(self):
        """
        Increments the count of modifications (`n_modifications`) in the statistics 
        and updates the repository.
        """
        stats = self.get()
        stats.n_modifications += 1
        return self.statsRepository.update(stats)