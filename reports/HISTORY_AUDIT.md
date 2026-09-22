# 历史记录查漏补缺（2026-09-22）

接入122条历史记录：97份顶层summary＋25份后期逐轮文件；原有v19替换导入，未重复追加。

- v15/v19：排除显式运行异常。
- v21 mixed best：2/6；v24 box best 2/16、box latest 3/16、mixed best 3/14；v25 bottle latest 3/6。
- 早期专项保留各自指标，不能统一解释为抓取成功。
- summary分母仅排除明确标注异常；不声称未标注异常已验证。
- 未重新计算逐物理步信号。历史handoff副本不重复接入。
- v20与v20c不可仅凭5/8相同数字认定同一实验；接入有逐轮证据的v20c，原v20仍需准确源文件。
- v22未执行模型不伪造0次实验记录。

## 仅索引、未计入成功率

- /home/shared-assets/yurui-test-eval/a2d_eval_test/a2d_eval_downloads_range_summary.json
- /home/shared-assets/yurui-test-eval/a2d_eval_test/a2d_eval_epoch40_range_summary.json

## 逐文件核对

| 文件 | 状态 | 成功/分母 | 原始尝试 |
|---|---|---:|---:|
| a2d_eval_download_5000_summary.json | 已接入 | 12/629 | 629 |
| a2d_eval_download_pilot_summary.json | 已接入 | 0/1 | 1 |
| a2d_eval_downloads_range_summary.json | 仅索引：缺少成功或完成计数 | —/— | — |
| a2d_eval_epoch40_5000_summary.json | 已接入 | 40/629 | 629 |
| a2d_eval_epoch40_pilot_summary.json | 已接入 | 0/1 | 1 |
| a2d_eval_epoch40_range_summary.json | 仅索引：缺少成功或完成计数 | —/— | — |
| a2d_hand_funnel_best_ema_50_summary.json | 已接入 | 1/2 | 2 |
| a2d_hand_funnel_latest_raw_50_summary.json | 已接入 | 0/1 | 1 |
| a2d_hand_funnel_v11_h16_grasp_lift_tiers_best_action_epoch40_500_summary.json | 已接入 | 2/3 | 3 |
| a2d_hand_funnel_v11_h16_grasp_lift_tiers_hand_target_best_ema_500_summary.json | 已接入 | 2/2 | 2 |
| a2d_hand_funnel_v11_h16_grasp_lift_tiers_hand_target_latest_raw_500_summary.json | 已接入 | 2/2 | 2 |
| a2d_hand_funnel_v11_h16_grasp_lift_tiers_latest_8_14_500_summary.json | 已接入 | 0/2 | 2 |
| a2d_hand_funnel_v12_h16_grasp_lift_5f_tiers_best_action_epoch40_500_summary.json | 已接入 | 20/65 | 65 |
| a2d_hand_funnel_v12_h16_grasp_lift_5f_tiers_hand_target_best_ema_500_summary.json | 已接入 | 49/65 | 65 |
| a2d_hand_funnel_v12_h16_grasp_lift_5f_tiers_hand_target_latest_raw_500_summary.json | 已接入 | 45/64 | 64 |
| a2d_hand_funnel_v12_h16_grasp_lift_5f_tiers_latest_8_14_500_summary.json | 已接入 | 30/65 | 65 |
| a2d_hand_funnel_v15_exclusive_horizon_4_8_12_16_5f_hand_target_best_ema_h12_500_summary.json | 已接入 | 4/7 | 500 |
| a2d_hand_funnel_v15_exclusive_horizon_4_8_12_16_5f_hand_target_best_ema_h16_500_summary.json | 已接入 | 4/7 | 500 |
| a2d_hand_funnel_v15_exclusive_horizon_4_8_12_16_5f_hand_target_best_ema_h4_500_summary.json | 已接入 | 7/8 | 500 |
| a2d_hand_funnel_v15_exclusive_horizon_4_8_12_16_5f_hand_target_best_ema_h8_500_summary.json | 已接入 | 6/7 | 500 |
| a2d_hand_funnel_v15_exclusive_horizon_4_8_12_16_5f_hand_target_latest_raw_h12_500_summary.json | 已接入 | 5/7 | 500 |
| a2d_hand_funnel_v15_exclusive_horizon_4_8_12_16_5f_hand_target_latest_raw_h16_500_summary.json | 已接入 | 6/7 | 500 |
| a2d_hand_funnel_v15_exclusive_horizon_4_8_12_16_5f_hand_target_latest_raw_h4_500_summary.json | 已接入 | 4/7 | 500 |
| a2d_hand_funnel_v15_exclusive_horizon_4_8_12_16_5f_hand_target_latest_raw_h8_500_summary.json | 已接入 | 4/7 | 500 |
| a2d_hand_funnel_v16_exclusive_success_video_horizon_4_8_12_16_5f_hand_target_best_ema_h12_500_summary.json | 已接入 | 36/58 | 58 |
| a2d_hand_funnel_v16_exclusive_success_video_horizon_4_8_12_16_5f_hand_target_best_ema_h16_500_summary.json | 已接入 | 39/57 | 57 |
| a2d_hand_funnel_v16_exclusive_success_video_horizon_4_8_12_16_5f_hand_target_best_ema_h4_500_summary.json | 已接入 | 33/58 | 58 |
| a2d_hand_funnel_v16_exclusive_success_video_horizon_4_8_12_16_5f_hand_target_best_ema_h8_500_summary.json | 已接入 | 43/58 | 58 |
| a2d_hand_funnel_v16_exclusive_success_video_horizon_4_8_12_16_5f_hand_target_latest_raw_h12_500_summary.json | 已接入 | 38/58 | 58 |
| a2d_hand_funnel_v16_exclusive_success_video_horizon_4_8_12_16_5f_hand_target_latest_raw_h16_500_summary.json | 已接入 | 37/57 | 57 |
| a2d_hand_funnel_v16_exclusive_success_video_horizon_4_8_12_16_5f_hand_target_latest_raw_h4_500_summary.json | 已接入 | 42/58 | 58 |
| a2d_hand_funnel_v16_exclusive_success_video_horizon_4_8_12_16_5f_hand_target_latest_raw_h8_500_summary.json | 已接入 | 38/58 | 58 |
| a2d_hand_funnel_v17_four_model_horizon_4_8_16_5f_hand_target_best_ema_h16_500_summary.json | 已接入 | 18/24 | 24 |
| a2d_hand_funnel_v17_four_model_horizon_4_8_16_5f_hand_target_best_ema_h4_500_summary.json | 已接入 | 13/25 | 25 |
| a2d_hand_funnel_v17_four_model_horizon_4_8_16_5f_hand_target_best_ema_h8_500_summary.json | 已接入 | 18/24 | 24 |
| a2d_hand_funnel_v17_four_model_horizon_4_8_16_5f_hand_target_epoch100_raw_h16_500_summary.json | 已接入 | 17/24 | 24 |
| a2d_hand_funnel_v17_four_model_horizon_4_8_16_5f_hand_target_epoch100_raw_h4_500_summary.json | 已接入 | 17/25 | 25 |
| a2d_hand_funnel_v17_four_model_horizon_4_8_16_5f_hand_target_epoch100_raw_h8_500_summary.json | 已接入 | 14/24 | 24 |
| a2d_hand_funnel_v17_four_model_horizon_4_8_16_5f_hand_target_latest_raw_h16_500_summary.json | 已接入 | 17/24 | 24 |
| a2d_hand_funnel_v17_four_model_horizon_4_8_16_5f_hand_target_latest_raw_h4_500_summary.json | 已接入 | 16/25 | 25 |
| a2d_hand_funnel_v17_four_model_horizon_4_8_16_5f_hand_target_latest_raw_h8_500_summary.json | 已接入 | 12/24 | 24 |
| a2d_hand_funnel_v17_four_model_horizon_4_8_16_5f_rgb_only_final_raw_h16_500_summary.json | 已接入 | 18/24 | 24 |
| a2d_hand_funnel_v17_four_model_horizon_4_8_16_5f_rgb_only_final_raw_h4_500_summary.json | 已接入 | 15/25 | 25 |
| a2d_hand_funnel_v17_four_model_horizon_4_8_16_5f_rgb_only_final_raw_h8_500_summary.json | 已接入 | 14/24 | 24 |
| a2d_hand_funnel_v19_cfm_dp_imle_nine_model_horizon_8_16_5f_cfm_post_best_ema_h16_500_summary.json | 已接入 | 11/17 | 500 |
| a2d_hand_funnel_v19_cfm_dp_imle_nine_model_horizon_8_16_5f_cfm_post_best_ema_h8_500_summary.json | 已接入 | 11/18 | 500 |
| a2d_hand_funnel_v19_cfm_dp_imle_nine_model_horizon_8_16_5f_cfm_post_best_raw_h16_500_summary.json | 已接入 | 12/17 | 500 |
| a2d_hand_funnel_v19_cfm_dp_imle_nine_model_horizon_8_16_5f_cfm_post_best_raw_h8_500_summary.json | 已接入 | 11/19 | 500 |
| a2d_hand_funnel_v19_cfm_dp_imle_nine_model_horizon_8_16_5f_cfm_post_latest_raw_h16_500_summary.json | 已接入 | 11/17 | 500 |
| a2d_hand_funnel_v19_cfm_dp_imle_nine_model_horizon_8_16_5f_cfm_post_latest_raw_h8_500_summary.json | 已接入 | 10/18 | 500 |
| a2d_hand_funnel_v19_cfm_dp_imle_nine_model_horizon_8_16_5f_dp_best_ema_h16_500_summary.json | 已接入 | 12/17 | 500 |
| a2d_hand_funnel_v19_cfm_dp_imle_nine_model_horizon_8_16_5f_dp_best_ema_h8_500_summary.json | 已接入 | 15/18 | 500 |
| a2d_hand_funnel_v19_cfm_dp_imle_nine_model_horizon_8_16_5f_dp_best_raw_h16_500_summary.json | 已接入 | 11/17 | 500 |
| a2d_hand_funnel_v19_cfm_dp_imle_nine_model_horizon_8_16_5f_dp_best_raw_h8_500_summary.json | 已接入 | 11/18 | 500 |
| a2d_hand_funnel_v19_cfm_dp_imle_nine_model_horizon_8_16_5f_dp_latest_raw_h16_500_summary.json | 已接入 | 10/17 | 500 |
| a2d_hand_funnel_v19_cfm_dp_imle_nine_model_horizon_8_16_5f_dp_latest_raw_h8_500_summary.json | 已接入 | 12/18 | 500 |
| a2d_hand_funnel_v19_cfm_dp_imle_nine_model_horizon_8_16_5f_imle_best_ema_h16_500_summary.json | 已接入 | 12/17 | 500 |
| a2d_hand_funnel_v19_cfm_dp_imle_nine_model_horizon_8_16_5f_imle_best_ema_h8_500_summary.json | 已接入 | 13/18 | 500 |
| a2d_hand_funnel_v19_cfm_dp_imle_nine_model_horizon_8_16_5f_imle_best_raw_h16_500_summary.json | 已接入 | 14/17 | 500 |
| a2d_hand_funnel_v19_cfm_dp_imle_nine_model_horizon_8_16_5f_imle_best_raw_h8_500_summary.json | 已接入 | 14/18 | 500 |
| a2d_hand_funnel_v19_cfm_dp_imle_nine_model_horizon_8_16_5f_imle_latest_raw_h16_500_summary.json | 已接入 | 13/16 | 500 |
| a2d_hand_funnel_v19_cfm_dp_imle_nine_model_horizon_8_16_5f_imle_latest_raw_h8_500_summary.json | 已接入 | 10/17 | 500 |
| a2d_hand_funnel_v2_best_ema_50_summary.json | 已接入 | 0/1 | 1 |
| a2d_hand_funnel_v2_latest_raw_50_summary.json | 已接入 | 1/1 | 1 |
| a2d_hand_funnel_v3_best_ema_50_summary.json | 已接入 | 2/4 | 4 |
| a2d_hand_funnel_v3_latest_raw_50_summary.json | 已接入 | 1/4 | 4 |
| a2d_hand_funnel_v4_best_ema_500_summary.json | 已接入 | 4/7 | 7 |
| a2d_hand_funnel_v4_downloads_500_summary.json | 已接入 | 1/7 | 7 |
| a2d_hand_funnel_v4_epoch40_500_summary.json | 已接入 | 5/7 | 7 |
| a2d_hand_funnel_v4_latest_raw_500_summary.json | 已接入 | 3/7 | 7 |
| a2d_hand_funnel_v5_strict_best_ema_500_summary.json | 已接入 | 11/136 | 136 |
| a2d_hand_funnel_v5_strict_downloads_500_summary.json | 已接入 | 1/137 | 137 |
| a2d_hand_funnel_v5_strict_epoch40_500_summary.json | 已接入 | 7/136 | 136 |
| a2d_hand_funnel_v5_strict_latest_raw_500_summary.json | 已接入 | 14/136 | 136 |
| a2d_hand_funnel_v6_strict_epoch40_500_summary.json | 已接入 | 4/40 | 40 |
| a2d_hand_funnel_v6_strict_latest_8_14_500_summary.json | 已接入 | 5/40 | 40 |
| a2d_hand_funnel_v6_strict_rgb_only_best_500_summary.json | 已接入 | 0/40 | 40 |
| a2d_hand_funnel_v6_strict_rgb_only_latest_500_summary.json | 已接入 | 1/39 | 39 |
| a2d_hand_funnel_v7_h16_strict_epoch40_500_summary.json | 已接入 | 2/6 | 6 |
| a2d_hand_funnel_v7_h16_strict_latest_8_14_500_summary.json | 已接入 | 1/6 | 6 |
| a2d_hand_funnel_v7_h16_strict_rgb_only_best_500_summary.json | 已接入 | 0/6 | 6 |
| a2d_hand_funnel_v7_h16_strict_rgb_only_latest_500_summary.json | 已接入 | 0/6 | 6 |
| a2d_hand_funnel_v8_h16_strict_best_action_epoch40_500_summary.json | 已接入 | 82/321 | 321 |
| a2d_hand_funnel_v8_h16_strict_best_val_epoch22_500_summary.json | 已接入 | 38/321 | 321 |
| a2d_hand_funnel_v8_h16_strict_latest_8_14_500_summary.json | 已接入 | 121/321 | 321 |
| a2d_hand_funnel_v8_h16_strict_level0_step25445_500_summary.json | 已接入 | 28/321 | 321 |
| a2d_hand_funnel_v8_h16_strict_rgb_only_latest_500_summary.json | 已接入 | 68/320 | 320 |
| a2d_hand_funnel_v9_h16_hand_target_strict_best_action_epoch40_500_summary.json | 已接入 | 83/323 | 323 |
| a2d_hand_funnel_v9_h16_hand_target_strict_hand_target_best_ema_500_summary.json | 已接入 | 0/2 | 2 |
| a2d_hand_funnel_v9_h16_hand_target_strict_hand_target_latest_raw_500_summary.json | 已接入 | 0/1 | 1 |
| a2d_hand_funnel_v9_h16_hand_target_strict_latest_8_14_500_summary.json | 已接入 | 121/323 | 323 |
| a2d_handshape_download_5000_summary.json | 已接入 | 3/204 | 204 |
| a2d_handshape_epoch40_5000_summary.json | 已接入 | 2/203 | 203 |
| a2d_prelift_arm_joints_download_5000_summary.json | 已接入 | 377/514 | 514 |
| a2d_prelift_arm_joints_epoch40_5000_summary.json | 已接入 | 496/514 | 514 |
| a2d_prelift_position_download_5000_summary.json | 已接入 | 7/9 | 9 |
| a2d_prelift_position_epoch40_5000_summary.json | 已接入 | 7/8 | 8 |
| a2d_wrap_download_5000_summary.json | 已接入 | 9/446 | 446 |
| a2d_wrap_epoch40_5000_summary.json | 已接入 | 34/446 | 446 |
| imle_mixed_latest_raw.jsonl | 已重算接入 | 3/7 | 8 |
| bottle_latest_raw.jsonl | 已重算接入 | 3/6 | 8 |
| bottle_best_raw.jsonl | 已重算接入 | 60/130 | 144 |
| bottle_latest_raw.jsonl | 已重算接入 | 64/138 | 144 |
| mixed_best_raw.jsonl | 已重算接入 | 25/127 | 136 |
| mixed_latest_raw.jsonl | 已重算接入 | 75/126 | 136 |
| mixed_latest_raw.jsonl | 已重算接入 | 5/7 | 8 |
| mixed_latest_raw.jsonl | 已重算接入 | 12/15 | 16 |
| mixed_best_raw.jsonl | 已重算接入 | 18/66 | 72 |
| mixed_latest_raw.jsonl | 已重算接入 | 38/58 | 64 |
| box_best_ema.jsonl | 已重算接入 | 5/7 | 8 |
| a2d_six_cfm_sequential_v21_smoke_20260904T1210_bottle_best_raw_h16_8.jsonl | 已重算接入 | 2/8 | 8 |
| a2d_six_cfm_sequential_v21_smoke_20260904T1210_bottle_latest_raw_h16_8.jsonl | 已重算接入 | 2/8 | 8 |
| a2d_six_cfm_sequential_v21_smoke_20260904T1210_box_best_ema_h16_8.jsonl | 已重算接入 | 6/8 | 8 |
| a2d_six_cfm_sequential_v21_smoke_20260904T1210_box_latest_raw_h16_8.jsonl | 已重算接入 | 7/8 | 8 |
| a2d_six_cfm_sequential_v21_smoke_20260904T1210_mixed_best_raw_h16_8.jsonl | 已重算接入 | 2/6 | 8 |
| a2d_six_cfm_sequential_v21_smoke_20260904T1210_mixed_latest_raw_h16_8.jsonl | 已重算接入 | 6/8 | 8 |
| a2d_six_cfm_sequential_v22_50ep_20260904_box_best_ema_h16_50.jsonl | 已重算接入 | 1/1 | 1 |
| a2d_six_cfm_sequential_v22_50ep_20260904_box_latest_raw_h16_50.jsonl | 已重算接入 | 1/1 | 1 |
| a2d_six_cfm_v24_b19_nongfu_gui_50ep_20260907_bottle_best_raw_h16_50.jsonl | 已重算接入 | 10/17 | 17 |
| a2d_six_cfm_v24_b19_nongfu_gui_50ep_20260907_bottle_latest_raw_h16_50.jsonl | 已重算接入 | 9/17 | 17 |
| a2d_six_cfm_v24_b19_nongfu_gui_50ep_20260907_box_best_ema_h16_50.jsonl | 已重算接入 | 2/16 | 17 |
| a2d_six_cfm_v24_b19_nongfu_gui_50ep_20260907_box_latest_raw_h16_50.jsonl | 已重算接入 | 3/16 | 17 |
| a2d_six_cfm_v24_b19_nongfu_gui_50ep_20260907_mixed_best_raw_h16_50.jsonl | 已重算接入 | 3/14 | 17 |
| a2d_six_cfm_v24_b19_nongfu_gui_50ep_20260907_mixed_latest_raw_h16_50.jsonl | 已重算接入 | 8/16 | 16 |
