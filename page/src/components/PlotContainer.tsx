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
import './PlotContainer.scss'
import { PlotScatterChart } from './PlotScatterChart.tsx'
import React from 'react'

export interface PlotContainerProps
{
  description: string,
  variable: string,
}

export function PlotContainer ({ description, variable } : PlotContainerProps)
{
  return (
    <>
      <div className='mx-auto d-block text-center plot-container'>

        <PlotScatterChart barName={variable} domainPadding={0} />

        <p>
          <i>{description}</i>
        </p>
      </div>
    </>)
}
