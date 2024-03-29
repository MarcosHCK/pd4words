/* Copyright (c) 2023-2025
 * This file is part of pd4words.
 *
 * pd4words is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * pd4words is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with pd4words. If not, see <http://www.gnu.org/licenses/>.
 */

export type PlotValues = Array<PlotValue>

export interface PlotProps
{
  barName: string,
}

export interface PlotValue
{
  x: number,
  y: number,
}

export interface PlotValueGroups
{
  complexity: PlotValues,
  length: PlotValues,
  repetitiveness: PlotValues,
}

export interface PlotValueLabeled extends PlotValue
{
  label: string,
}

export function plotIsLabeled (obj: any): obj is PlotValueLabeled
{
  return obj && typeof obj.name === 'string' && typeof obj.label === 'string'
}
