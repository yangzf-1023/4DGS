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
 --output_dir 0913/factor0.996_decay_exp_k2 --opacity_decay --opacity_decay_factor 0.996 \ 
  --factor_decay --factor_decay_mode exp --k 2

# factor0.996_decay_exp_k0.5
CUDA_VISIBLE_DEVICES=1 python train.py --config configs/dynerf/flame_steak.yaml --training_view 1,10,13,20 \
 --output_dir 0913/factor0.996_decay_exp_k0.5 --opacity_decay --opacity_decay_factor 0.996 \
  --factor_decay --factor_decay_mode exp --k 0.5

# factor0.996_decay_sin
CUDA_VISIBLE_DEVICES=1 python train.py --config configs/dynerf/flame_steak.yaml --training_view 1,10,13,20 \
 --output_dir 0913/factor0.996_decay_sin --opacity_decay --opacity_decay_factor 0.996 \
  --factor_decay --factor_decay_mode sin

# factor0.996_decay_exp_k1
CUDA_VISIBLE_DEVICES=1 python train.py --config configs/dynerf/flame_steak.yaml --training_view 1,10,13,20 \
 --output_dir 0913/factor0.996_decay_exp_k1 --opacity_decay --opacity_decay_factor 0.996 \
  --factor_decay --factor_decay_mode exp --k 1

# factor0.996_decay_exp_k1_warm_up
CUDA_VISIBLE_DEVICES=1 python train.py --config configs/dynerf/flame_steak.yaml --training_view 1,10,13,20 \
 --output_dir 0913/factor0.996_decay_exp_k1_warm_up --opacity_decay --opacity_decay_factor 0.996 \
  --factor_decay --factor_decay_mode exp --k 1 --warm_up

# mlp0.996
CUDA_VISIBLE_DEVICES=1 python train.py --config configs/dynerf/flame_steak.yaml --training_view 1,10,13,20 \
 --output_dir 0913/mlp0.996 --opacity_decay --opacity_decay_mode mlp --opacity_decay_factor 0.996

# factor0.996_decay_exp_k1_gradient
CUDA_VISIBLE_DEVICES=1 python train.py --config configs/dynerf/flame_steak.yaml --training_view 1,10,13,20 \
 --output_dir 0913/factor0.996_decay_exp_k1_gradient --opacity_decay --opacity_decay_factor 0.996 \
  --factor_decay --factor_decay_mode exp --k 1 --gradient

# 0914 

# factor0.9965_decay_exp_k1
CUDA_VISIBLE_DEVICES=1 python train.py --config configs/dynerf/flame_steak.yaml --training_view 1,10,13,20 \
 --output_dir 0914/factor0.9965_decay_exp_k1 --opacity_decay --opacity_decay_factor 0.9965 \
  --factor_decay --factor_decay_mode exp --k 1

# factor0.996_decay_exp_k1_warm_up_until3000
CUDA_VISIBLE_DEVICES=1 python train.py --config configs/dynerf/flame_steak.yaml --training_view 1,10,13,20 \
 --output_dir 0914/factor0.996_decay_exp_k1_warm_up_until3000 --opacity_decay --opacity_decay_factor 0.996 \
  --factor_decay --factor_decay_mode exp --k 1 --warm_up --warm_up_until 3000

# mlp0.9965_coefficient_lr1e-6
CUDA_VISIBLE_DEVICES=1 python train.py --config configs/dynerf/flame_steak.yaml --training_view 1,10,13,20 \
 --output_dir 0914/mlp0.9965 --opacity_decay --opacity_decay_mode mlp --opacity_decay_factor 0.9965 --coefficient_lr 1e-6

# factor0.995_decay_exp_k1
CUDA_VISIBLE_DEVICES=1 python train.py --config configs/dynerf/flame_steak.yaml --training_view 1,10,13,20 \
 --output_dir 0914/factor0.995_decay_exp_k1 --opacity_decay --opacity_decay_factor 0.995 \
  --factor_decay --factor_decay_mode exp --k 1

# 0915

# exp0.996_p0_offset0
CUDA_VISIBLE_DEVICES=1 python train.py --config configs/dynerf/flame_steak.yaml --training_view 1,10,13,20 \
 --output_dir 0915/exp0.996_p0_offset0 --opacity_decay_mode exp --opacity_decay --opacity_decay_factor 0.996 --p 0 --offset 0.0

# exp0.996_p2_offset0
CUDA_VISIBLE_DEVICES=1 python train.py --config configs/dynerf/flame_steak.yaml --training_view 1,10,13,20 \
 --output_dir 0915/exp0.996_p2_offset0 --opacity_decay_mode exp --opacity_decay --opacity_decay_factor 0.996 --p 2 --offset 0.0

# exp0.996_p-2_offset0
CUDA_VISIBLE_DEVICES=1 python train.py --config configs/dynerf/flame_steak.yaml --training_view 1,10,13,20 \
 --output_dir 0915/exp0.996_p-2_offset0 --opacity_decay_mode exp --opacity_decay --opacity_decay_factor 0.996 --p -2 --offset 0.0

# factor0.9965_decay_exp_k1
CUDA_VISIBLE_DEVICES=1 python train.py --config configs/dynerf/flame_steak.yaml --training_view 1,10,13,20 \
 --output_dir 0915/factor0.9965_decay_exp_k1 --opacity_decay --opacity_decay_factor 0.9965 \
  --factor_decay --factor_decay_mode exp --k 1

# mlp0.9955
CUDA_VISIBLE_DEVICES=1 python train.py --config configs/dynerf/flame_steak.yaml --training_view 1,10,13,20 \
 --output_dir 0915/mlp0.9955 --opacity_decay --opacity_decay_mode mlp --opacity_decay_factor 0.9955

# mlp0.9955_factor_decay
CUDA_VISIBLE_DEVICES=1 python train.py --config configs/dynerf/flame_steak.yaml --training_view 1,10,13,20 \
 --output_dir 0915/mlp0.9955_factor_decay --opacity_decay --opacity_decay_mode mlp --opacity_decay_factor 0.9955 \
  --factor_decay --factor_decay_mode exp --k 1

# 0916

# exp0.995-0.998_p2_offset0
CUDA_VISIBLE_DEVICES=1 python train.py --config configs/dynerf/flame_steak.yaml --training_view 1,10,13,20 \
 --output_dir 0916/exp0.996_p2_offset0 --opacity_decay_mode exp --opacity_decay --opacity_decay_factor 0.997 --p 2 --offset 0.002

# exp0.995-0.998_p2_offset0.002_factor_decay
CUDA_VISIBLE_DEVICES=1 python train.py --config configs/dynerf/flame_steak.yaml --training_view 1,10,13,20 \
 --output_dir 0916/exp0.996_p2_offset0.002_factor_decay --opacity_decay_mode exp --opacity_decay --opacity_decay_factor 0.997 --p 2 --offset 0.002 \
 --factor_decay --factor_decay_mode exp --k 1

# 0917

# power_desc0.995-1_p2
CUDA_VISIBLE_DEVICES=2 python train.py --config configs/dynerf/flame_steak.yaml --training_view 1,10,13,20 \
 --output_dir 0917/power_desc0.995-1_p2 --opacity_decay --opacity_decay_mode power_desc --f_min 0.995 --f_max 1.0 --p 2 

# power_asc0.995-1_p2
CUDA_VISIBLE_DEVICES=2 python train.py --config configs/dynerf/flame_steak.yaml --training_view 1,10,13,20 \
 --output_dir 0917/power_asc0.995-1_p2 --opacity_decay --opacity_decay_mode power_asc --f_min 0.995 --f_max 1.0 --p 2 

# decay0.997
CUDA_VISIBLE_DEVICES=1 python train.py --config configs/dynerf/flame_steak.yaml --training_view 1,10,13,20 \
 --output_dir 0917/decay0.997 --opacity_decay --opacity_decay_mode const --f_min 0.997

# decay0.9975
CUDA_VISIBLE_DEVICES=1 python train.py --config configs/dynerf/flame_steak.yaml --training_view 1,10,13,20 \
 --output_dir 0917/decay0.9975 --opacity_decay --opacity_decay_mode const --f_min 0.9975

# decay0.9975_gradient
CUDA_VISIBLE_DEVICES=1 python train.py --config configs/dynerf/flame_steak.yaml --training_view 1,10,13,20 \
 --output_dir 0917/decay0.9975_gradient --opacity_decay --opacity_decay_mode const --f_min 0.9975 --gradient

# decay0.998
CUDA_VISIBLE_DEVICES=1 python train.py --config configs/dynerf/flame_steak.yaml --training_view 1,10,13,20 \
 --output_dir 0917/decay0.998 --opacity_decay --opacity_decay_mode const --f_min 0.998



```
