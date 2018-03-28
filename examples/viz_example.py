#!/usr/bin/env python

# Python imports.
from __future__ import print_function
import argparse

# Other imports.
import srl_example_setup
from simple_rl.agents import QLearningAgent
from simple_rl.run_experiments import run_single_agent_on_mdp 
from simple_rl.tasks import FourRoomMDP
from simple_rl.tasks.grid_world.GridWorldMDPClass import make_grid_world_from_file
from simple_rl.planning import ValueIteration

def parse_args():
    # Add all arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", type=str, default="value", nargs='?', help="Choose the visualization type (one of {value, policy, agent}).")
    args = parser.parse_args()
    return args.v

def main():
    # Setup MDP, Agents.
    mdp = FourRoomMDP(5, 5, goal_locs=[(5, 5)], gamma=0.99, step_cost=0.01)
    # mdp = make_grid_world_from_file("octogrid.txt", num_goals=12, randomize=False)
    ql_agent = QLearningAgent(mdp.get_actions(), epsilon=0.2)
    viz = parse_args()
    viz = "learning"

    if viz == "value":
        # Run experiment and make plot.
        mdp.visualize_value()
    elif viz == "policy":
        # Viz policy
        value_iter = ValueIteration(mdp)
        value_iter.run_vi()
        policy = value_iter.policy
        mdp.visualize_policy(policy)
    elif viz == "agent":
        # Solve problem and show agent interaction.
        print("\n", str(ql_agent), "interacting with", str(mdp))
        run_single_agent_on_mdp(ql_agent, mdp, episodes=500, steps=200)
        mdp.visualize_agent(ql_agent)
    elif viz == "learning":
        # Run experiment and make plot.
        mdp.visualize_learning(ql_agent)

if __name__ == "__main__":
    main()
