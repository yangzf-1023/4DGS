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
CUDA_VISIBLE_DEVICES=4 python train.py --config configs/dynerf/flame_steak.yaml --training_view 1,10,13,20 \
 --output_dir 0912/factor0.9965 --opacity_decay --opacity_decay_factor 0.9965

# factor0.996
CUDA_VISIBLE_DEVICES=5 python train.py --config configs/dynerf/flame_steak.yaml --training_view 1,10,13,20 \
 --output_dir 0912/factor0.996 --opacity_decay --opacity_decay_factor 0.996

# factor0.996_decay
CUDA_VISIBLE_DEVICES=5 python train.py --config configs/dynerf/flame_steak.yaml --training_view 1,10,13,20 \
 --output_dir 0912/factor0.996_decay --opacity_decay --opacity_decay_factor 0.996 --factor_decay

# factor0.9955
CUDA_VISIBLE_DEVICES=6 python train.py --config configs/dynerf/flame_steak.yaml --training_view 1,10,13,20 \
 --output_dir 0912/factor0.9955 --opacity_decay --opacity_decay_factor 0.9955

# factor0.995
CUDA_VISIBLE_DEVICES=7 python train.py --config configs/dynerf/flame_steak.yaml --training_view 1,10,13,20 \
 --output_dir 0912/factor0.995 --opacity_decay --opacity_decay_factor 0.995

# factor0.995_decay
CUDA_VISIBLE_DEVICES=7 python train.py --config configs/dynerf/flame_steak.yaml --training_view 1,10,13,20 \
 --output_dir 0912/factor0.995_decay --opacity_decay --opacity_decay_factor 0.995 --factor_decay

```
