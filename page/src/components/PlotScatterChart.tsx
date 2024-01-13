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
import { PlotProps, PlotValues } from '../services/Plot.tsx'
import { useStats } from '../services/StatsProvider.tsx'
import { VictoryChart, VictoryChartProps, VictoryLine, VictoryScatter, VictoryTheme } from 'victory'
import React, { useEffect, useState } from 'react'

export function PlotScatterChart ({ barName, ...rest } : PlotProps & VictoryChartProps)
{
  const [ plotValueGroups, broken ] = useStats ()
  const [ trendLine, setTrendLine ] = useState<PlotValues | undefined> ()

  useEffect (() =>
    {
      if (plotValueGroups !== undefined && broken === undefined)
        {
          const dots : PlotValues = plotValueGroups[barName]
          const count : number = dots.length

          let sumX = 0, sumY = 0
          let sumXX = 0, sumXY = 0

          for (let i = 0; i < count; i++)
            {
              sumX += dots[i].x
              sumY += dots[i].y
              sumXX += dots[i].x * dots[i].x
              sumXY += dots[i].x * dots[i].y
            }

          const m = (count * sumXY - sumX * sumY) / (count * sumXX - sumX * sumX)
          const b = (sumY - m * sumX) / count

          setTrendLine
            ([
              { x: Math.min (...dots.map (d => d.x)),
                y: m * Math.min (...dots.map (d => d.x)) + b },
              { x: Math.max (...dots.map (d => d.x)),
                y: m * Math.max (...dots.map (d => d.x)) + b },
            ])
        }
    }, [barName, broken, plotValueGroups])

  if (broken !== undefined)
    return <Alert color='danger'>Data acquisition failed!</Alert>
  else if (plotValueGroups === undefined || trendLine === undefined)
    return <Alert color='primary'>Please wait...</Alert>
  else
    return (
      <>
        <VictoryChart theme={VictoryTheme.material} scale={{ x: 'linear', y: 'linear' }} {...rest}>
          <VictoryLine data={trendLine} style={{ data: { strokeWidth: 1 } }} />
          <VictoryScatter data={plotValueGroups[barName]} size={1} />
        </VictoryChart>
      </>)
}
