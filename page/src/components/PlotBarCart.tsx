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
import { Alert } from 'reactstrap'
import { useStats } from '../services/StatsProvider.tsx'
import { VictoryBar, VictoryChart, VictoryChartProps, VictoryTheme } from 'victory'
import React from 'react'

export interface PlotBarChartProps extends VictoryChartProps
{
  barName: string,
}

export function PlotBarChart ({ barName, ...rest } : PlotBarChartProps)
{
  const [ plotBars, broken ] = useStats ()

  if (broken !== undefined)
    return <Alert color='danger'>Data acquisition failed!</Alert>
  else if (plotBars === undefined)
    return <Alert color='primary'>Please wait...</Alert>
  else
    return (
      <>
        <VictoryChart theme={VictoryTheme.material} scale={{ x: 'linear', y: 'linear' }} {...rest}>
          <VictoryBar data={plotBars[barName]} x='year' y='value' />
        </VictoryChart>
      </>)
}
