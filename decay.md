# 针对于每次迭代的修改版

```shell

# 0911

# decay0.9965
CUDA_VISIBLE_DEVICES=0 python train.py --config configs/dynerf/flame_steak.yaml --training_view 1,10,13,20 \
 --output_dir 0911/decay0.9965 --opacity_decay --opacity_decay_factor 0.9965

# decay0.995
CUDA_VISIBLE_DEVICES=0 python train.py --config configs/dynerf/flame_steak.yaml --training_view 1,10,13,20 \
 --output_dir 0911/decay0.995 --opacity_decay --opacity_decay_factor 0.995

# decay0.995_until30000
CUDA_VISIBLE_DEVICES=0 python train.py --config configs/dynerf/flame_steak.yaml --training_view 1,10,13,20 \
 --output_dir 0911/decay0.995_until30000 --opacity_decay --opacity_decay_factor 0.995 

# decay0.995_factor_decay
CUDA_VISIBLE_DEVICES=0 python train.py --config configs/dynerf/flame_steak.yaml --training_view 1,10,13,20 \
 --output_dir 0911/decay0.995_factor_decay --opacity_decay --opacity_decay_factor 0.995 --factor_decay

# decay0.995_factor_decay_until30000
CUDA_VISIBLE_DEVICES=0 python train.py --config configs/dynerf/flame_steak.yaml --training_view 1,10,13,20 \
 --output_dir 0911/decay0.995_factor_decay_until30000 --opacity_decay --opacity_decay_factor 0.995 

# 0912

# factor0.9965
CUDA_VISIBLE_DEVICES=1 python train.py --config configs/dynerf/flame_steak.yaml --training_view 1,10,13,20 \
 --output_dir 0912/factor0.9965 --opacity_decay --opacity_decay_factor 0.9965

# factor0.996
CUDA_VISIBLE_DEVICES=1 python train.py --config configs/dynerf/flame_steak.yaml --training_view 1,10,13,20 \
 --output_dir 0912/factor0.996 --opacity_decay --opacity_decay_factor 0.996

# factor0.996_decay
CUDA_VISIBLE_DEVICES=1 python train.py --config configs/dynerf/flame_steak.yaml --training_view 1,10,13,20 \
 --output_dir 0912/factor0.996_decay --opacity_decay --opacity_decay_factor 0.996 --factor_decay

# factor0.9955
CUDA_VISIBLE_DEVICES=1 python train.py --config configs/dynerf/flame_steak.yaml --training_view 1,10,13,20 \
 --output_dir 0912/factor0.9955 --opacity_decay --opacity_decay_factor 0.9955

# factor0.995
CUDA_VISIBLE_DEVICES=1 python train.py --config configs/dynerf/flame_steak.yaml --training_view 1,10,13,20 \
 --output_dir 0912/factor0.995 --opacity_decay --opacity_decay_factor 0.995

# factor0.995_decay
CUDA_VISIBLE_DEVICES=1 python train.py --config configs/dynerf/flame_steak.yaml --training_view 1,10,13,20 \
 --output_dir 0912/factor0.995_decay --opacity_decay --opacity_decay_factor 0.995 --factor_decay

# 0913

# factor0.996_decay_exp_k2
CUDA_VISIBLE_DEVICES=1 python train.py --config configs/dynerf/flame_steak.yaml --training_view 1,10,13,20 \
 --output_dir 0913/factor0.996_decay_exp_k2 --opacity_decay --opacity_decay_factor 0.996 --factor_decay --factor_decay_mode exp --k 2

# factor0.996_decay_exp_k0.5
CUDA_VISIBLE_DEVICES=1 python train.py --config configs/dynerf/flame_steak.yaml --training_view 1,10,13,20 \
 --output_dir 0913/factor0.996_decay_exp_k0.5 --opacity_decay --opacity_decay_factor 0.996 --factor_decay --factor_decay_mode exp --k 0.5

# factor0.996_decay_sin
CUDA_VISIBLE_DEVICES=1 python train.py --config configs/dynerf/flame_steak.yaml --training_view 1,10,13,20 \
 --output_dir 0913/factor0.996_decay_sin --opacity_decay --opacity_decay_factor 0.996 --factor_decay --factor_decay_mode sin

# factor0.996_decay_exp_k1
CUDA_VISIBLE_DEVICES=1 python train.py --config configs/dynerf/flame_steak.yaml --training_view 1,10,13,20 \
 --output_dir 0913/factor0.996_decay_exp_k1 --opacity_decay --opacity_decay_factor 0.996 --factor_decay --factor_decay_mode exp --k 1

# factor0.996_decay_exp_k1_warm_up
CUDA_VISIBLE_DEVICES=1 python train.py --config configs/dynerf/flame_steak.yaml --training_view 1,10,13,20 \
 --output_dir 0913/factor0.996_decay_exp_k1_warm_up --opacity_decay --opacity_decay_factor 0.996 --factor_decay --factor_decay_mode exp --k 1 --warm_up

```
