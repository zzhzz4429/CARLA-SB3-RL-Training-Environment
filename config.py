import torch as th

from utils import lr_schedule

_CONFIG_PPO = {
    "algorithm": "PPO",
    "algorithm_params": dict(
        learning_rate=lr_schedule(1e-4, 1e-7, 5),
        gae_lambda=0.95,
        clip_range=0.2,
        ent_coef=0.05,
        n_epochs=10,
        n_steps=1024,
        policy_kwargs=dict(activation_fn=th.nn.ReLU,
                           net_arch=[dict(pi=[500, 300], vf=[500, 300])])
    ),
    "state": ["steer", "throttle", "speed", "angle_next_waypoint", "maneuver"],
    "vae_model": "vae_64",
    "action_smoothing": 0.75,
    "reward_fn": "reward_fn5",
    "reward_params": dict(
        min_speed=20.0,  # km/h
        max_speed=35.0,  # km/h
        target_speed=25.0,  # kmh
        max_distance=3.0,  # Max distance from center before terminating
        max_std_center_lane=0.4,
        max_angle_center_lane=90,
        penalty_reward=-10,
    ),
    "obs_res": (160, 80),
    "seed": 436,
}

_CONFIG_PPO_FINE_TUNING = {
    "algorithm": "PPO",
    "algorithm_params": dict(
        learning_rate=1e-5,
        gae_lambda=0.95,
        clip_range=0.3,
        ent_coef=0.3,
        n_epochs=15,
        n_steps=1024,
        policy_kwargs=dict(activation_fn=th.nn.ReLU,
                           net_arch=[dict(pi=[500, 300], vf=[500, 300])])
    ),
    "state": ["steer", "throttle", "speed", "angle_next_waypoint", "maneuver"],
    "vae_model": "vae_64",
    "action_smoothing": 0.75,
    "reward_fn": "reward_fn5",
    "reward_params": dict(
        min_speed=20.0,  # km/h
        max_speed=35.0,  # km/h
        target_speed=25.0,  # kmh
        max_distance=3.0,  # Max distance from center before terminating
        max_std_center_lane=0.4,
        max_angle_center_lane=90,
        penalty_reward=-10,
    ),
    "obs_res": (160, 80),
    "seed": 5314,
}
# n_actions = env.action_space.shape[-1]
# action_noise = NormalActionNoise(mean=np.zeros(n_actions), sigma=0.5 * np.ones(n_actions))
# model = DDPG('CnnPolicy', env, verbose=1, action_noise=action_noise, buffer_size=10000, tensorboard_log=log_dir, device='cpu')
# dqn_hyperparam = dict(
#     batch_size=100,
#     buffer_size=20_000,
#     target_update_interval=48,
#     exploration_fraction=0.3,
#     learning_starts=5_000,
#     train_freq=4
# )
CONFIG = _CONFIG_PPO_FINE_TUNING