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

const reportWebVitals = onPerfEntry =>
{
  if (onPerfEntry && onPerfEntry instanceof Function)
    {
      import ('web-vitals').then (
  ({ getCLS, getFID, getFCP, getLCP, getTTFB }) =>
        {
          getCLS(onPerfEntry)
          getFID(onPerfEntry)
          getFCP(onPerfEntry)
          getLCP(onPerfEntry)
          getTTFB(onPerfEntry)
        })
    }
}

export default reportWebVitals
