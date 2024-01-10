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
import { avg_repetitiveness } from '../services/Stats.tsx'
import { createContext, useContext } from 'react'
import { PlotBars, PlotSteps } from '../services/Stats.tsx'
import { Stats } from '../services/Stats.tsx'
import { total_complexity } from '../services/Stats.tsx'
import { total_length } from '../services/Stats.tsx'
import React, { useEffect, useState } from 'react'
const statsContext = createContext<StatsProviderValue> ([undefined, undefined])

export type StatsProviderValue = [ PlotBars | undefined, string | undefined ]

export function useStats ()
{
  return useContext (statsContext)
}

export function StatsProvider (props)
{
  const { children } = props
  const [ broken, setBroken ] = useState<string | undefined> ()
  const [ plotBars, setPlotBars ] = useState<PlotBars | undefined> ()

  useEffect (() =>
    {
      const processData = async (stats : Stats) =>
        {
          let complexity_r : PlotSteps = []
          let length_r : PlotSteps = []
          let repetitiveness_r : PlotSteps = []
          let max_length = 0

          for (const year in stats)
            {
              const books = stats[year]
              const complexity = total_complexity (books)
              const length = total_length (books)
              const repetitiveness = avg_repetitiveness (books)

              max_length = length > max_length ? length : max_length

              complexity_r = [{value: complexity, year: Number (year)}, ...complexity_r]
              length_r = [{value: length, year: Number (year)}, ...length_r]
              repetitiveness_r = [{value: repetitiveness, year: Number (year)}, ...repetitiveness_r]
            }

          length_r = length_r.map (step => { return { ...step, value: step.value / max_length } })
        return {complexity: complexity_r, length: length_r, repetitiveness: repetitiveness_r}
        }

      if (plotBars === undefined && broken === undefined)
        {
          fetch ('/article.json')
            .then (response => response.json ())
            .then (json => processData (json))
            .then (data => setPlotBars (data))
            .catch (reason => { setBroken (reason) })
        }
    // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [])

  return (
    <>
      <statsContext.Provider
        value={[plotBars, broken]}>
          {children}
      </statsContext.Provider>
    </>)
}
