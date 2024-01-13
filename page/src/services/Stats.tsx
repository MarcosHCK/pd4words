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

export type BookStats = [ string, StatsDigest ]
export type YearStats = Array<BookStats>

export interface Stats
{
  [year : number] : YearStats,
}

export interface StatsDigest
{
  complexity : number,
  length : number,
  repetitiveness : number,
}

export function avg_repetitiveness (books : YearStats)
{
  let total = 0
  let count = books.length

  books.forEach (([, digest]) =>
    {
      total += digest.repetitiveness
    })
return total / count
}

export function total_complexity (books : YearStats)
{
  let total = 0
  let count = total_length (books)

  books.forEach (([, digest]) =>
    {
      total += digest.complexity
    })
return total / count
}

export function total_length (books : YearStats)
{
  let total = 0

  books.forEach (([, digest]) =>
    {
      total += digest.length
    })
return total
}
