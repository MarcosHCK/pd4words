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
import './Portrait.scss'
import { Container } from 'reactstrap'
import React from 'react'

export interface PortraitProps
{
  alt?: string,
  description?: string,
  src: string,
}

export function Portrait ({ alt = '', description = '', src } : PortraitProps)
{
  return (
    <>
      <Container className='text-center portrait'>

        <img alt={alt} className='mx-auto d-block portrait' src={src} />

        <p className='portrait'>
          <i>{description}</i>
        </p>
      </Container>
    </>)
}
