/*
 * Copyright (C) 2021-2024 ETH Zurich and University of Bologna
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

/**
 * Authors: Davide Nadalini
*/ 

/**
 * @brief Structure for interpolators. Interpolation factor is defined automatically by H, W tensor sizes.
 * @param input blob structure for the input data 
 * @param output blob structure for the output data 
 * @param interpolate_data if == 1, downsamples the data (channelwise)
 * @param interpolate_gradient if == 1, downsamples the gradient (channelwise)
 */
struct interpolation_args {
    struct blob *input;
    struct blob *output;
    int interpolate_data;
    int interpolate_gradient;
};

/**
 * Functions to be called
 */

/**
 * @brief Nearest Neighbour interpolation. Call this function in you code.
 * @param interpolation_args pointer to a interpolation_args structure
 */
void pulp_nearest_neighbour_interpolation_fp32_cl (void * interpolation_args);

/**
 * @brief Bilinear interpolation. Call this function in you code.
 * @param interpolation_args pointer to a interpolation_args structure
 */
void pulp_bilinear_interpolation_fp32_cl (void * interpolation_args);


/**
 * Paralellizable core functions
 */

/**
 * @brief Core function to be parallelized with pi_cl_team_fork(NUM_CORES, pulp_nearest_neighbour_core_fp32, &interpolation_args);
 * @param interpolation_args pointer to a interpolation_args structure
 */
void pulp_nearest_neighbour_core_fp32 (void * interpolation_args);

/**
 * @brief Core function to be parallelized with pi_cl_team_fork(NUM_CORES, pulp_bilinear_core_fp32, &interpolation_args);
 * @param interpolation_args pointer to a interpolation_args structure
 */
void pulp_bilinear_core_fp32 (void * interpolation_args);
