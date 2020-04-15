from typing import Any, Callable, Dict, Sequence, TypeVar

from mesa_behaviors.agents.base_agent import BaseAgent


# type var F is a type constraint on Agent Features
F = TypeVar("F")
AgentPopulation = Sequence[BaseAgent[Any, Any, F]]
AgentLabel = str
AgentLabels = Sequence[AgentLabel]
Distribution = Callable[[AgentLabels, int], AgentLabels]
AgentGenerator = Callable[[], BaseAgent[Any, Any, F]]
AgentTypeMap = Dict[AgentLabel, AgentGenerator[F]]
AgentPopulationGenerator = Callable[[], AgentPopulation[F]]


def generate_population(
    distribution: Distribution, agent_types: AgentTypeMap[F], size: int
) -> AgentPopulationGenerator[F]:
    def generate() -> Sequence[BaseAgent[Any, Any, F]]:
        distribution_list = distribution(list(agent_types.keys()), size)
        agents = [
            agent_types[label]().set_id(ind)
            for ind, label in enumerate(distribution_list)
        ]
        if len(agents) != size:
            raise ValueError("Distribution did not meet population requirements")
        return agents

    return generate
