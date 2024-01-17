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
import '../bootstrap.scss'
import { Container, Navbar } from 'reactstrap'
import { localUrl } from '../services/Url.tsx'
import { PlotContainer } from './PlotContainer.tsx'
import { Portrait } from './Portrait.tsx'
import { StatsProvider } from '../services/StatsProvider.tsx'
import React from 'react'

export function Article ()
{
  /* ÁÉÍÓÚÑáéíóúñ¿¡ */

  return (
    <>

      <header>

        <Navbar className="navbar-expand-sm ng-white border-bottom mb-3" container light>

          <h1>Libros cuánticos</h1>

        </Navbar>

      </header>

      <Container tag='main'>

        <hr className='divider' />

        <StatsProvider source={localUrl ('article.json')}>

          <div>

            <p className='indented-paragraph'>
              El arte contemporáneo es usualmente percibido como "simple". Ciertamente, en comparación con movimientos anteriores el arte contemporáneo es menos
              ornamentado. Por ejemplo, las grandes obras pictóricas clásicas se caracterizan por su profundo detalle, con fondos tan llenos de significado y vida
              como sus objetos centrales. Sin embargo, el arte contemporáneo impacta por su minimalismo.
            </p>

            <Portrait src={localUrl ('Virgen de las Rocas.jpg')} description='La Virgen de las Rocas, Leonardo Da Vinci, 1483-1486' />
            <Portrait src={localUrl ('The Gathering Anguish Strikes Beneath.jpg')} description='The Gathering Anguish Strikes Beneath..., John Murphy, 1945' />

            <p className='indented-paragraph'>
              Para los artistas es un reflejo de las complejidades y distracciones de la vida moderna, donde los artistas buscan deshacerse del exceso y centrarse
              en los elementos esenciales del arte. El minimalismo también permite una mayor accesibilidad y compromiso con el arte, ya que los espectadores no se
              sienten abrumados por detalles recargados u ornamentados. Además, la simplicidad del arte contemporáneo a menudo refleja un deseo de honestidad y
              autenticidad, y los artistas rechazan la pretensión y el exceso de los movimientos artísticos anteriores.
            </p>

            <p className='indented-paragraph'>
              Ahora, ¿qué pasa en la literatura? ¿podemos hacerse un libro minimalista? Puede ser difícil de creer, pero justamente eso es lo que está pasando en
              la actualidad (y desde hace un buen tiempo).
              De la forma más minimalista posible (ya que es el tema por qué no aprovecharlo) analizaremos las características cambiantes de la obra literaria
              moderna (a partir de 1900) a través de tres métricas: la complejidad, en cuanto a lo inusual que son las palabras utilizadas en la prosa, la
              longitud del texto, y la diversidad del vocabulario.
            </p>

          </div>

          <hr className='divider' />

          <div>

            <div>

              <PlotContainer description='Complejidad promedio por año' variable='complexity' />

              <p className='indented-paragraph' >
                Es interesante como la complejidad del lenguaje usado en un libro influye en su atractivo para el lector: aunque ciertas personas puedan disfrutar de
                un lenguaje complejo (principalmente si se usa como dispositivo narrativo), una comunicación en términos simples es preferible.
                Como se aprecia en el gráfico la complejidad del lenguaje usado en las obras desde 1900 está en constante, aunque no muy pronunciada, disminución.
                Es evidente que actualmente el lector prefiere un lenguaje sencillo que transmita las mismas ideas.
              </p>
            </div>

            <hr className='divider' />

            <div>

              <PlotContainer description='Longitud promedio por año' variable='length' />

              <p className='indented-paragraph' >
                La longitud es la siguiente métrica a analizar. No son necesarias demasiadas ceremonias, es una medida común.
                En contraste con la complejidad, la longitud aumentó mucho más rápido a lo largo del siglo.
              </p>
            </div>

            <hr className='divider' />

            <div>

              <PlotContainer description='Diversidad promedio por año' variable='repetitiveness' />

              <p className='indented-paragraph' >
                Finalmente, la diversidad del texto refleja la razón entre la longitud y la cantidad de palabras diferentes que posee el texto analizado. Esta métrica
                es particularmente interesante porque da una pista sobre su calidad (una novela compuesta de solo un puñado de palabras difícilmente puede
                transmitir información de forma efectiva).
                Esta vez se puede apreciar que la diversidad del lenguaje en las obras del siglo pasado (y parte de este) declinó rápidamente de forma constante.
              </p>
            </div>

            <hr className='divider' />

            <div>
              <h4>Metodología</h4>

              <p className='indented-paragraph'>
                Para medir los diversos parámetros de cada año se usó una muestra de los libros publicados en él. Para la medición de la complejidad se usó un dataset
                proporcionado por <a href='https://wortschatz.uni-leipzig.de/'>Leipzig Corpora Collection</a> para asociar una métrica a cada palabra, entendida como
                una medida de lo común que es su uso, luego calcula una puntuación a cada libro sobre lo mucho o poco que utiliza las palabras poco comunes. La longitud y
                diversidad del lenguaje se midieron contando las palabras individuales del cada libro, con lo que se calcula la longitud, y luego la diversidad como la
                razón entre su longitud y la cantidad de palabras diferentes usadas; las palabras se extrajeron usando <a href='https://www.nltk.org/'>NLTK</a>, una
                herramienta disponible para Python.
              </p>
            </div>

            <hr className='divider' />

            <footer>
              <Navbar className="navbar-expand-sm ng-white mb-3" container light>
                <h6>
                  Copyright (C) 2024 Marcos Antonio Pérez Lorenzo

                  <br />
                  <small>
                    <a href='https://github.com/MarcosHCK/pd4words/'>Fuente</a>
                  </small>
                </h6>
                <p>
                  <i>Los contenidos expuestos están bajo licencia <a href='https://www.gnu.org/licenses/gpl-3.0.txt'>GNU GPLv3</a></i>
                </p>
              </Navbar>
            </footer>

          </div>
        </StatsProvider>
      </Container>
    </>)
}
