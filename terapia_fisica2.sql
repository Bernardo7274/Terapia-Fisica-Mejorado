-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 09-12-2024 a las 18:03:54
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `terapia_fisica2`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `antecedentesheredofamiliares`
--

CREATE TABLE `antecedentesheredofamiliares` (
  `id_ficha` int(11) DEFAULT NULL,
  `enfermedad` varchar(50) DEFAULT NULL,
  `si` tinyint(1) DEFAULT 0,
  `no` tinyint(1) DEFAULT 0,
  `parentesco` varchar(100) DEFAULT NULL,
  `vivo` tinyint(1) DEFAULT 0,
  `muerto` tinyint(1) DEFAULT 0,
  `otro` text DEFAULT NULL,
  `observaciones` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `antecedentesheredofamiliares`
--

INSERT INTO `antecedentesheredofamiliares` (`id_ficha`, `enfermedad`, `si`, `no`, `parentesco`, `vivo`, `muerto`, `otro`, `observaciones`) VALUES
(242591, 'Cáncer', 1, 0, 'Hola', 0, 1, 'sdafdsfdsfsadf', 'sdafdsfdsfsadf'),
(242591, 'Diabetes', 0, 1, 'sdafdsfdsfsadf', 1, 0, 'sdafdsfdsfsadf', 'sdafdsfdsfsadf'),
(242591, 'Hipertensión', 1, 0, 'sdafdsfdsfsadf', 0, 1, 'sdafdsfdsfsadf', 'sdafdsfdsfsadf'),
(242591, 'Enfermedades Cardiacas', 0, 1, 'sdafdsfdsfsadf', 1, 0, 'sdafdsfdsfsadf', 'sdafdsfdsfsadf'),
(242591, 'Enfermedades Mentales', 1, 0, 'sdafdsfdsfsadf', 0, 1, 'sdafdsfdsfsadf', 'sdafdsfdsfsadf'),
(242591, 'Alergias', 0, 1, 'sdafdsfdsfsadf', 1, 0, 'sdafdsfdsfsadf', 'sdafdsfdsfsadf');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `antecedentespersonalesnopatologicos`
--

CREATE TABLE `antecedentespersonalesnopatologicos` (
  `id_ficha` int(11) DEFAULT NULL,
  `PropiaRenta` varchar(255) DEFAULT NULL,
  `Ventilacion` varchar(255) DEFAULT NULL,
  `Iluminacion` varchar(255) DEFAULT NULL,
  `Piso` varchar(255) DEFAULT NULL,
  `Electrodomesticos` varchar(255) DEFAULT NULL,
  `Servicios` varchar(255) DEFAULT NULL,
  `DescripcionVivienda` text DEFAULT NULL,
  `NoComidasDia` int(11) DEFAULT NULL,
  `AguaLts` float DEFAULT NULL,
  `GruposAlimenticios` varchar(255) DEFAULT NULL,
  `DescripcionRutinaAlimenticia` text DEFAULT NULL,
  `HigieneBucal` varchar(255) DEFAULT NULL,
  `BanosDia` int(11) DEFAULT NULL,
  `CambiosRopa` varchar(255) DEFAULT NULL,
  `ActividadFisica` varchar(255) DEFAULT NULL,
  `Deporte` varchar(255) DEFAULT NULL,
  `Ocio` varchar(255) DEFAULT NULL,
  `Ocupacion` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `antecedentespersonalesnopatologicos`
--

INSERT INTO `antecedentespersonalesnopatologicos` (`id_ficha`, `PropiaRenta`, `Ventilacion`, `Iluminacion`, `Piso`, `Electrodomesticos`, `Servicios`, `DescripcionVivienda`, `NoComidasDia`, `AguaLts`, `GruposAlimenticios`, `DescripcionRutinaAlimenticia`, `HigieneBucal`, `BanosDia`, `CambiosRopa`, `ActividadFisica`, `Deporte`, `Ocio`, `Ocupacion`) VALUES
(242591, 'Hola', 'sdafdsfdsfsadf', 'sdafdsfdsfsadf', 'sdafdsfdsfsadf', 'sdafdsfdsfsadf', 'sdafdsfdsfsadf', 'sdafdsfdsfsadf', 2, 74.5, 'sdafdsfdsfsadf', 'sdafdsfdsfsadf', 'sdafdsfdsfsadf', 7, '7', 'sdafdsfdsfsadf', 'sdafdsfdsfsadf', 'sdafdsfdsfsadf', 'sdafdsfdsfsadf');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `antecedentes_ginecobstetricos`
--

CREATE TABLE `antecedentes_ginecobstetricos` (
  `id_ficha` int(11) DEFAULT NULL,
  `menarquia` varchar(255) DEFAULT NULL,
  `fecha_ultima_menstruacion` date DEFAULT NULL,
  `caracteristicas_menstruacion` text DEFAULT NULL,
  `inicio_vida_sexual` date DEFAULT NULL,
  `uso_anticonceptivos` varchar(255) DEFAULT NULL,
  `numero_embarazos` int(11) DEFAULT NULL,
  `numero_partos` int(11) DEFAULT NULL,
  `numero_cesareas` int(11) DEFAULT NULL,
  `observaciones` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `antecedentes_ginecobstetricos`
--

INSERT INTO `antecedentes_ginecobstetricos` (`id_ficha`, `menarquia`, `fecha_ultima_menstruacion`, `caracteristicas_menstruacion`, `inicio_vida_sexual`, `uso_anticonceptivos`, `numero_embarazos`, `numero_partos`, `numero_cesareas`, `observaciones`) VALUES
(242591, 'Hola', '2024-12-25', 'sdafdsfdsfsadf', '2024-12-05', 'sdafdsfdsfsadf', 4, 4, 4, 'sdafdsfdsfsadf');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `antecedentes_padecimientoactual`
--

CREATE TABLE `antecedentes_padecimientoactual` (
  `id_ficha` int(11) NOT NULL,
  `descripcion` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `antecedentes_padecimientoactual`
--

INSERT INTO `antecedentes_padecimientoactual` (`id_ficha`, `descripcion`) VALUES
(242591, 'Hola');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `antecedentes_patologicos`
--

CREATE TABLE `antecedentes_patologicos` (
  `id_ficha` int(11) DEFAULT NULL,
  `patologia` varchar(255) DEFAULT NULL,
  `si` tinyint(1) DEFAULT NULL,
  `no` tinyint(1) DEFAULT NULL,
  `edad_presentacion` int(11) DEFAULT NULL,
  `secuelas_complicaciones` text DEFAULT NULL,
  `inmunizaciones` text DEFAULT NULL,
  `observaciones` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `antecedentes_patologicos`
--

INSERT INTO `antecedentes_patologicos` (`id_ficha`, `patologia`, `si`, `no`, `edad_presentacion`, `secuelas_complicaciones`, `inmunizaciones`, `observaciones`) VALUES
(242591, 'Traumatismos', 0, 1, 3, 'Hola', 'sdafdsfdsfsadf', 'sdafdsfdsfsadf'),
(242591, 'Cirugías', 1, 0, 3, 'sdafdsfdsfsadf', 'sdafdsfdsfsadf', 'sdafdsfdsfsadf'),
(242591, 'Luxaciones', 0, 1, 3, 'sdafdsfdsfsadf', 'sdafdsfdsfsadf', 'sdafdsfdsfsadf'),
(242591, 'Alergias', 0, 1, 3, 'sdafdsfdsfsadf', 'sdafdsfdsfsadf', 'sdafdsfdsfsadf'),
(242591, 'Toxicomanías', 0, 1, 3, 'sdafdsfdsfsadf', 'sdafdsfdsfsadf', 'sdafdsfdsfsadf'),
(242591, 'Padecimientos psiquiátricos', 1, 0, 3, 'sdafdsfdsfsadf', 'sdafdsfdsfsadf', 'sdafdsfdsfsadf');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ciclo_marcha_miembro_inferior`
--

CREATE TABLE `ciclo_marcha_miembro_inferior` (
  `id_ficha` int(11) DEFAULT NULL,
  `fase_apoyo_completo` varchar(255) DEFAULT NULL,
  `contacto_talon_izquierdo` varchar(255) DEFAULT NULL,
  `contacto_talon_derecho` varchar(255) DEFAULT NULL,
  `apoyo_plantar_izquierdo` varchar(255) DEFAULT NULL,
  `apoyo_plantar_derecho` varchar(255) DEFAULT NULL,
  `apoyo_medio_izquierdo` varchar(255) DEFAULT NULL,
  `apoyo_medio_derecho` varchar(255) DEFAULT NULL,
  `fase_oscilacion_completo` varchar(255) DEFAULT NULL,
  `balanceo_inicial_izquierdo` varchar(255) DEFAULT NULL,
  `balanceo_inicial_derecho` varchar(255) DEFAULT NULL,
  `balanceo_medio_izquierdo` varchar(255) DEFAULT NULL,
  `balanceo_medio_derecho` varchar(255) DEFAULT NULL,
  `balanceo_terminal_izquierdo` varchar(255) DEFAULT NULL,
  `balanceo_terminal_derecho` varchar(255) DEFAULT NULL,
  `rotacion_pelvica_completo` varchar(255) DEFAULT NULL,
  `inclinacion_pelvica_completo` varchar(255) DEFAULT NULL,
  `flexion_rodilla_izquierdo` varchar(255) DEFAULT NULL,
  `flexion_rodilla_derecho` varchar(255) DEFAULT NULL,
  `movimientos_coordinados_rodilla_tobillo_izquierdo` varchar(255) DEFAULT NULL,
  `movimientos_coordinados_rodilla_tobillo_derecho` varchar(255) DEFAULT NULL,
  `movimiento_centro_gravedad_completo` varchar(255) DEFAULT NULL,
  `cadencia_completo` varchar(255) DEFAULT NULL,
  `balanceo_ms_completo` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `ciclo_marcha_miembro_inferior`
--

INSERT INTO `ciclo_marcha_miembro_inferior` (`id_ficha`, `fase_apoyo_completo`, `contacto_talon_izquierdo`, `contacto_talon_derecho`, `apoyo_plantar_izquierdo`, `apoyo_plantar_derecho`, `apoyo_medio_izquierdo`, `apoyo_medio_derecho`, `fase_oscilacion_completo`, `balanceo_inicial_izquierdo`, `balanceo_inicial_derecho`, `balanceo_medio_izquierdo`, `balanceo_medio_derecho`, `balanceo_terminal_izquierdo`, `balanceo_terminal_derecho`, `rotacion_pelvica_completo`, `inclinacion_pelvica_completo`, `flexion_rodilla_izquierdo`, `flexion_rodilla_derecho`, `movimientos_coordinados_rodilla_tobillo_izquierdo`, `movimientos_coordinados_rodilla_tobillo_derecho`, `movimiento_centro_gravedad_completo`, `cadencia_completo`, `balanceo_ms_completo`) VALUES
(242591, 'Hola', 'sdafdsfdsfsadf', 'sdafdsfdsfsadf', 'sdafdsfdsfsadf', 'sdafdsfdsfsadf', 'sdafdsfdsfsadf', 'sdafdsfdsfsadf', 'sdafdsfdsfsadf', 'sdafdsfdsfsadf', 'sdafdsfdsfsadf', 'sdafdsfdsfsadf', 'sdafdsfdsfsadf', 'sdafdsfdsfsadf', 'sdafdsfdsfsadf', 'sdafdsfdsfsadf', 'sdafdsfdsfsadf', 'sdafdsfdsfsadf', 'sdafdsfdsfsadf', 'sdafdsfdsfsadf', 'sdafdsfdsfsadf', 'sdafdsfdsfsadf', 'sdafdsfdsfsadf', 'sdafdsfdsfsadf');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `exploracion`
--

CREATE TABLE `exploracion` (
  `id_ficha` int(11) NOT NULL,
  `habitus_exterior` varchar(255) DEFAULT NULL,
  `peso` decimal(5,2) DEFAULT NULL,
  `altura` decimal(5,2) DEFAULT NULL,
  `imc` decimal(5,2) DEFAULT NULL,
  `temperatura` decimal(4,2) DEFAULT NULL,
  `pulso_cardiaco` int(11) DEFAULT NULL,
  `frecuencia_respiratoria` int(11) DEFAULT NULL,
  `presion_arterial` varchar(50) DEFAULT NULL,
  `saturacion_oxigeno` decimal(4,2) DEFAULT NULL,
  `observaciones` text DEFAULT NULL,
  `resultados_previos_actuales` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `exploracion`
--

INSERT INTO `exploracion` (`id_ficha`, `habitus_exterior`, `peso`, `altura`, `imc`, `temperatura`, `pulso_cardiaco`, `frecuencia_respiratoria`, `presion_arterial`, `saturacion_oxigeno`, `observaciones`, `resultados_previos_actuales`) VALUES
(242591, 'Hola', 4.50, 4.50, 89.90, 8.50, 5, 6, '2', 4.00, 'sdafdsfdsfsadf', 'sdafdsfdsfsadf');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ficha_identificaciones`
--

CREATE TABLE `ficha_identificaciones` (
  `id` int(11) NOT NULL,
  `fecha_elaboracion` date DEFAULT NULL,
  `nombre_paciente` varchar(255) DEFAULT NULL,
  `genero` varchar(25) DEFAULT NULL,
  `folio` int(11) DEFAULT NULL,
  `edad` int(11) DEFAULT NULL,
  `fecha_nacimiento` date DEFAULT NULL,
  `lugar_nacimiento` varchar(255) DEFAULT NULL,
  `ocupacion` varchar(255) DEFAULT NULL,
  `domicilio_actual` varchar(300) DEFAULT NULL,
  `estado_civil` varchar(20) DEFAULT NULL,
  `nacionalidad` varchar(20) DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `contacto_emergencia_nombre` varchar(255) DEFAULT NULL,
  `contacto_emergencia_telefono` varchar(20) DEFAULT NULL,
  `diagnostico_medico` text DEFAULT NULL,
  `elaboro_historial_clinico` varchar(255) DEFAULT NULL,
  `motivo_consulta` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `ficha_identificaciones`
--

INSERT INTO `ficha_identificaciones` (`id`, `fecha_elaboracion`, `nombre_paciente`, `genero`, `folio`, `edad`, `fecha_nacimiento`, `lugar_nacimiento`, `ocupacion`, `domicilio_actual`, `estado_civil`, `nacionalidad`, `telefono`, `contacto_emergencia_nombre`, `contacto_emergencia_telefono`, `diagnostico_medico`, `elaboro_historial_clinico`, `motivo_consulta`) VALUES
(242591, '2024-12-06', 'Bernardo', 'femenino', 242576, 23, '2024-12-06', 'sdafdsfdsfsadf', 'sdafdsfdsfsadf', 'sdafdsfdsfsadf', 'soltero', 'sdafdsfdsfsadf', '9988776644', 'sdafdsfdsfsadf', '9988776655', 'sdafdsfdsfsadf', 'sdafdsfdsfsadf', 'sdafdsfdsfsadf');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `fuerza_muscular_cabeza_y_torax`
--

CREATE TABLE `fuerza_muscular_cabeza_y_torax` (
  `id_ficha` int(11) DEFAULT NULL,
  `movimiento` varchar(255) DEFAULT NULL,
  `valores_obtenidos` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `fuerza_muscular_cabeza_y_torax`
--

INSERT INTO `fuerza_muscular_cabeza_y_torax` (`id_ficha`, `movimiento`, `valores_obtenidos`) VALUES
(242591, 'Extensión de cabeza', 'Hola'),
(242591, 'Extensión de cuello', 'sdafdsfdsfsadf'),
(242591, 'Extensión conjunta', 'sdafdsfdsfsadf'),
(242591, 'Flexión de cabeza', 'sdafdsfdsfsadf'),
(242591, 'Flexión de cuello', 'sdafdsfdsfsadf'),
(242591, 'Flexión conjunta', 'sdafdsfdsfsadf'),
(242591, 'Flexión y rotación conjuntas', 'sdafdsfdsfsadf'),
(242591, 'Rotación del cuello', 'sdafdsfdsfsadf'),
(242591, 'Observaciones', 'sdafdsfdsfsadf');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `fuerza_muscular_cabeza_y_torax1`
--

CREATE TABLE `fuerza_muscular_cabeza_y_torax1` (
  `id_ficha` int(11) DEFAULT NULL,
  `movimiento` varchar(255) DEFAULT NULL,
  `valores_obtenidos` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `fuerza_muscular_cabeza_y_torax1`
--

INSERT INTO `fuerza_muscular_cabeza_y_torax1` (`id_ficha`, `movimiento`, `valores_obtenidos`) VALUES
(242591, 'Extensión lumbar', 'Hola'),
(242591, 'Extensión torácica', 'sdafdsfdsfsadf'),
(242591, 'Elevación pélvica', 'sdafdsfdsfsadf'),
(242591, 'Flexión', 'sdafdsfdsfsadf'),
(242591, 'Rotación', 'sdafdsfdsfsadf'),
(242591, 'Inspiración', 'sdafdsfdsfsadf'),
(242591, 'Espiración forzada indirecta', 'sdafdsfdsfsadf');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `fuerza_muscular_miembro_inferior`
--

CREATE TABLE `fuerza_muscular_miembro_inferior` (
  `id_ficha` int(11) DEFAULT NULL,
  `derecha` varchar(255) DEFAULT NULL,
  `movimiento` varchar(255) DEFAULT NULL,
  `izquierda` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `fuerza_muscular_miembro_inferior`
--

INSERT INTO `fuerza_muscular_miembro_inferior` (`id_ficha`, `derecha`, `movimiento`, `izquierda`) VALUES
(242591, 'Hola', 'Flexión de cadera', 'Hola'),
(242591, 'sdafdsfdsfsadf', 'Extensión de la cadera', 'sdafdsfdsfsadf'),
(242591, 'sdafdsfdsfsadf', 'Abducción de la cadera', 'sdafdsfdsfsadf'),
(242591, 'sdafdsfdsfsadf', 'Aducción de la cadera', 'sdafdsfdsfsadf'),
(242591, 'sdafdsfdsfsadf', 'Rotación externa de la cadera', 'sdafdsfdsfsadf'),
(242591, 'sdafdsfdsfsadf', 'Rotación interna de la cadera', 'sdafdsfdsfsadf'),
(242591, 'sdafdsfdsfsadf', 'Flexión de la rodilla', 'sdafdsfdsfsadf'),
(242591, 'sdafdsfdsfsadf', 'Extensión de la rodilla', 'sdafdsfdsfsadf'),
(242591, 'sdafdsfdsfsadf', 'Flexión plantar del tobillo', 'sdafdsfdsfsadf'),
(242591, 'sdafdsfdsfsadf', 'Dorsiflexión e inversión del pie', 'sdafdsfdsfsadf'),
(242591, 'sdafdsfdsfsadf', 'Inversión del pie', 'sdafdsfdsfsadf'),
(242591, 'sdafdsfdsfsadf', 'Eversión del pie con flexión plantar', 'sdafdsfdsfsadf'),
(242591, 'sdafdsfdsfsadf', 'Eversión del pie con dorsiflexión', 'sdafdsfdsfsadf');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `fuerza_muscular_miembro_superior`
--

CREATE TABLE `fuerza_muscular_miembro_superior` (
  `id_ficha` int(11) DEFAULT NULL,
  `derecha` varchar(255) DEFAULT NULL,
  `movimiento` varchar(255) DEFAULT NULL,
  `izquierda` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `fuerza_muscular_miembro_superior`
--

INSERT INTO `fuerza_muscular_miembro_superior` (`id_ficha`, `derecha`, `movimiento`, `izquierda`) VALUES
(242591, 'Hola', 'Abducción y rotación superior de la escápula', 'Hola'),
(242591, 'sdafdsfdsfsadf', 'Elevación de la escápula', 'sdafdsfdsfsadf'),
(242591, 'sdafdsfdsfsadf', 'Aducción de la escápula', 'sdafdsfdsfsadf'),
(242591, 'sdafdsfdsfsadf', 'Aducción y descenso escapular', 'sdafdsfdsfsadf'),
(242591, 'sdafdsfdsfsadf', 'Aducción y rotación inferior de la escápula', 'sdafdsfdsfsadf'),
(242591, 'sdafdsfdsfsadf', 'Flexión del hombro', 'sdafdsfdsfsadf'),
(242591, 'sdafdsfdsfsadf', 'Extensión de hombro', 'sdafdsfdsfsadf'),
(242591, 'sdafdsfdsfsadf', 'Abducción del hombro', 'sdafdsfdsfsadf'),
(242591, 'sdafdsfdsfsadf', 'Abducción horizontal del hombro', 'sdafdsfdsfsadf'),
(242591, 'sdafdsfdsfsadf', 'Aducción horizontal del hombro', 'sdafdsfdsfsadf'),
(242591, 'sdafdsfdsfsadf', 'Rotación externa del hombro', 'sdafdsfdsfsadf'),
(242591, 'sdafdsfdsfsadf', 'Rotación interna del hombro', 'sdafdsfdsfsadf'),
(242591, 'sdafdsfdsfsadf', 'Flexión de codo', 'sdafdsfdsfsadf'),
(242591, 'sdafdsfdsfsadf', 'Extensión de codo', 'sdafdsfdsfsadf'),
(242591, 'sdafdsfdsfsadf', 'Supinación del antebrazo', 'sdafdsfdsfsadf'),
(242591, 'sdafdsfdsfsadf', 'Pronación del antebrazo', 'sdafdsfdsfsadf'),
(242591, 'sdafdsfdsfsadf', 'Flexión de la muñeca', 'sdafdsfdsfsadf'),
(242591, 'sdafdsfdsfsadf', 'Extensión de la muñeca', 'sdafdsfdsfsadf');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `goniometria_cabeza_y_torax`
--

CREATE TABLE `goniometria_cabeza_y_torax` (
  `id_ficha` int(11) DEFAULT NULL,
  `rangos_normales` varchar(255) DEFAULT NULL,
  `movimientos` varchar(255) DEFAULT NULL,
  `resultados` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `goniometria_cabeza_y_torax`
--

INSERT INTO `goniometria_cabeza_y_torax` (`id_ficha`, `rangos_normales`, `movimientos`, `resultados`) VALUES
(242591, '0-35°/45°', 'Flexión', 'Hola'),
(242591, '0-35°/45°', 'Extensión', 'sdafdsfdsfsadf'),
(242591, '0°-45°', 'Inclinación lateral derecha', 'sdafdsfdsfsadf'),
(242591, '0°-45°', 'Inclinación lateral izquierda', 'sdafdsfdsfsadf'),
(242591, '0-60°/80°', 'Rotación derecha', 'sdafdsfdsfsadf'),
(242591, '0-60°/80°', 'Rotación izquierda', 'sdafdsfdsfsadf'),
(242591, '*método de Schober', 'Flexión', 'sdafdsfdsfsadf'),
(242591, '0-30°', 'Extensión', 'sdafdsfdsfsadf'),
(242591, '0-30°/40°', 'Inclinación lateral derecha', 'sdafdsfdsfsadf'),
(242591, '0°-30°/40°', 'Inclinación lateral izquierda', 'sdafdsfdsfsadf'),
(242591, '0-30°', 'Rotación derecha', 'sdafdsfdsfsadf'),
(242591, '0-30°', 'Rotación izquierda', 'sdafdsfdsfsadf');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `goniometria_miembro_inferior`
--

CREATE TABLE `goniometria_miembro_inferior` (
  `id_ficha` int(11) DEFAULT NULL,
  `rango_normal` varchar(50) DEFAULT NULL,
  `izquierdo` varchar(50) DEFAULT NULL,
  `movimiento` varchar(50) DEFAULT NULL,
  `derecho` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `goniometria_miembro_inferior`
--

INSERT INTO `goniometria_miembro_inferior` (`id_ficha`, `rango_normal`, `izquierdo`, `movimiento`, `derecho`) VALUES
(242591, '0°-140°', 'Hola', 'Flexión de cadera', 'Hola'),
(242591, '0°-10°', 'sdafdsfdsfsadf', 'Extensión de cadera', 'sdafdsfdsfsadf'),
(242591, '0°-50°', 'sdafdsfdsfsadf', 'Abducción de cadera', 'sdafdsfdsfsadf'),
(242591, '0°-30°', 'sdafdsfdsfsadf', 'Aducción de cadera', 'sdafdsfdsfsadf'),
(242591, '0°-50°', 'sdafdsfdsfsadf', 'Rotación externa de cadera', 'sdafdsfdsfsadf'),
(242591, '0°-40°', 'sdafdsfdsfsadf', 'Rotación interna de cadera', 'sdafdsfdsfsadf'),
(242591, '0°-150°', 'sdafdsfdsfsadf', 'Flexión de rodilla', 'sdafdsfdsfsadf'),
(242591, '0°(activa)-10°(pasiva)', 'sdafdsfdsfsadf', 'Extensión de rodilla', 'sdafdsfdsfsadf'),
(242591, '0°-50°', 'sdafdsfdsfsadf', 'Plantiflexión', 'sdafdsfdsfsadf'),
(242591, '0°-30°', 'sdafdsfdsfsadf', 'Dorsiflexión', 'sdafdsfdsfsadf'),
(242591, '0°-60°', 'sdafdsfdsfsadf', 'Inversión del pie', 'sdafdsfdsfsadf'),
(242591, '0°-30°', 'sdafdsfdsfsadf', 'Eversión del pie', 'sdafdsfdsfsadf');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `goniometria_miembro_superior`
--

CREATE TABLE `goniometria_miembro_superior` (
  `id_ficha` int(11) DEFAULT NULL,
  `rango_normal` varchar(50) DEFAULT NULL,
  `izquierdo` varchar(50) DEFAULT NULL,
  `movimiento` varchar(50) DEFAULT NULL,
  `derecho` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `goniometria_miembro_superior`
--

INSERT INTO `goniometria_miembro_superior` (`id_ficha`, `rango_normal`, `izquierdo`, `movimiento`, `derecho`) VALUES
(242591, '0°-150°/170°', 'Hola', 'Flexión de hombro', 'Hola'),
(242591, '0°-40°', 'sdafdsfdsfsadf', 'Extensión de hombro', 'sdafdsfdsfsadf'),
(242591, '0-160°/180°', 'sdafdsfdsfsadf', 'Abducción de hombro', 'sdafdsfdsfsadf'),
(242591, '0°-30°', 'sdafdsfdsfsadf', 'Aducción de hombro', 'sdafdsfdsfsadf'),
(242591, '0°-70°', 'sdafdsfdsfsadf', 'Rotación externa de hombro', 'sdafdsfdsfsadf'),
(242591, '0°-70°', 'sdafdsfdsfsadf', 'Rotación interna de hombro', 'sdafdsfdsfsadf'),
(242591, '0°-150°', 'sdafdsfdsfsadf', 'Flexión de codo', 'sdafdsfdsfsadf'),
(242591, '0°(activa)-10°(pasiva)', 'sdafdsfdsfsadf', 'Extensión de codo', 'sdafdsfdsfsadf'),
(242591, '0°-90°', 'sdafdsfdsfsadf', 'Supinación del antebrazo', 'sdafdsfdsfsadf'),
(242591, '0°-90°', 'sdafdsfdsfsadf', 'Pronación del antebrazo', 'sdafdsfdsfsadf'),
(242591, '0°-25°-30°', 'sdafdsfdsfsadf', 'Desviación radial de muñeca', 'sdafdsfdsfsadf'),
(242591, '0°-30°-40°', 'sdafdsfdsfsadf', 'Desviación cubital de la muñeca', 'sdafdsfdsfsadf'),
(242591, '0°-50°/60°', 'sdafdsfdsfsadf', 'Flexión de muñeca', 'sdafdsfdsfsadf'),
(242591, '0°-35°/60°', 'sdafdsfdsfsadf', 'Extensión de muñeca', 'sdafdsfdsfsadf');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inicio_sesion`
--

CREATE TABLE `inicio_sesion` (
  `id` int(11) NOT NULL,
  `correo_electronico` varchar(255) DEFAULT NULL,
  `contraseña` varchar(255) DEFAULT NULL,
  `rol` int(11) UNSIGNED DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `inicio_sesion`
--

INSERT INTO `inicio_sesion` (`id`, `correo_electronico`, `contraseña`, `rol`) VALUES
(12, '202100140@upqroo.edu.mx', 'scrypt:32768:8:1$xduP0GhpUfBxNNIe$12fcec1f92fed77a5d015b1be2c51bd82a2520d42b32f14d3413d1ed7e9a4062080bdef40f09bc7fed656df264ea2f95c29de06ba5b55501d00be8c716590c4d', 1),
(46, '202100150@upqroo.edu.mx', 'scrypt:32768:8:1$aTZVOTNkRS3T6jrO$f26b8fca68870fc0f52af1ab6b406cbc4de7092871d1fb53d4639fc1446b9cd93d5704aa67c23f7c215967db7558c67f606f3b5f26c1752f8f58621c7d929de3', 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `notas_seguimientos`
--

CREATE TABLE `notas_seguimientos` (
  `id_ficha` int(11) DEFAULT NULL,
  `nombre` varchar(255) DEFAULT NULL,
  `diagnostico` varchar(255) DEFAULT NULL,
  `folio` varchar(10) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `numero_sesion` int(11) DEFAULT NULL,
  `notas` text DEFAULT NULL,
  `sugerencias_observaciones` text DEFAULT NULL,
  `nombreYfirma_tratante` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `notas_seguimientos`
--

INSERT INTO `notas_seguimientos` (`id_ficha`, `nombre`, `diagnostico`, `folio`, `fecha`, `numero_sesion`, `notas`, `sugerencias_observaciones`, `nombreYfirma_tratante`) VALUES
(242591, 'Maria', 'sdafdsfdsfsadf', '5289', '2024-12-08', 11, 'sdafdsfdsfsadf', 'sdafdsfdsfsadf', 'sdafdsfdsfsadf'),
(242591, 'Hola', 'sdfsdfsdfsdfsdaf', '7853', '2024-12-09', 6, 'fsdfdsfsdfsdaf', 'sdsdfsadfsadf', 'sdfsadfasdf');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `partes_cuerpo`
--

CREATE TABLE `partes_cuerpo` (
  `id` int(11) NOT NULL,
  `Nombre` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `partes_cuerpo`
--

INSERT INTO `partes_cuerpo` (`id`, `Nombre`) VALUES
(1, 'Miembros Superiores'),
(2, 'Miembros Inferiores'),
(3, 'Cabeza y cuello'),
(4, 'Columna, toráx y abdomen');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `partes_cuerpo_cabeza_y_torax`
--

CREATE TABLE `partes_cuerpo_cabeza_y_torax` (
  `id_ficha` int(11) DEFAULT NULL,
  `id_partes` int(11) DEFAULT NULL,
  `observacion` varchar(50) DEFAULT NULL,
  `palpacion` varchar(50) DEFAULT NULL,
  `descripcion` varchar(50) DEFAULT NULL,
  `dolor` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `partes_cuerpo_cabeza_y_torax`
--

INSERT INTO `partes_cuerpo_cabeza_y_torax` (`id_ficha`, `id_partes`, `observacion`, `palpacion`, `descripcion`, `dolor`) VALUES
(242591, 3, 'Hola1', 'sdafdsfdsfsadf', 'sdafdsfdsfsadf', 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `partes_cuerpo_cabeza_y_torax1`
--

CREATE TABLE `partes_cuerpo_cabeza_y_torax1` (
  `id_ficha` int(11) DEFAULT NULL,
  `id_partes` int(11) DEFAULT NULL,
  `observacion` varchar(50) DEFAULT NULL,
  `palpacion` varchar(50) DEFAULT NULL,
  `descripcion` varchar(50) DEFAULT NULL,
  `dolor` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `partes_cuerpo_cabeza_y_torax1`
--

INSERT INTO `partes_cuerpo_cabeza_y_torax1` (`id_ficha`, `id_partes`, `observacion`, `palpacion`, `descripcion`, `dolor`) VALUES
(242591, 4, 'Hola', 'sdafdsfdsfsadf', 'sdafdsfdsfsadf', 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `partes_cuerpo_miembro_inferior`
--

CREATE TABLE `partes_cuerpo_miembro_inferior` (
  `id_ficha` int(11) DEFAULT NULL,
  `id_partes` int(11) DEFAULT NULL,
  `observacion` varchar(50) DEFAULT NULL,
  `palpacion` varchar(50) DEFAULT NULL,
  `descripcion` varchar(50) DEFAULT NULL,
  `dolor` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `partes_cuerpo_miembro_inferior`
--

INSERT INTO `partes_cuerpo_miembro_inferior` (`id_ficha`, `id_partes`, `observacion`, `palpacion`, `descripcion`, `dolor`) VALUES
(242591, 2, 'Hola1', 'sdafdsfdsfsadf', 'sdafdsfdsfsadf', 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `partes_cuerpo_miembro_superior`
--

CREATE TABLE `partes_cuerpo_miembro_superior` (
  `id_ficha` int(11) DEFAULT NULL,
  `id_partes` int(11) DEFAULT NULL,
  `observacion` varchar(50) DEFAULT NULL,
  `palpacion` varchar(50) DEFAULT NULL,
  `descripcion` varchar(50) DEFAULT NULL,
  `dolor` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `partes_cuerpo_miembro_superior`
--

INSERT INTO `partes_cuerpo_miembro_superior` (`id_ficha`, `id_partes`, `observacion`, `palpacion`, `descripcion`, `dolor`) VALUES
(242591, 1, 'Hola', 'sdafdsfdsfsadf', 'sdafdsfdsfsadf', 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `plan_tratamientos`
--

CREATE TABLE `plan_tratamientos` (
  `id_ficha` int(11) DEFAULT NULL,
  `objetivo` varchar(255) DEFAULT NULL,
  `modalidad_terapeutica` varchar(255) DEFAULT NULL,
  `descripcion` text DEFAULT NULL,
  `dosis` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `plan_tratamientos`
--

INSERT INTO `plan_tratamientos` (`id_ficha`, `objetivo`, `modalidad_terapeutica`, `descripcion`, `dosis`) VALUES
(242591, 'Hola1', 'Hola1', 'Hola1', 'Hola1'),
(242591, 'sdafdsfdsfsadf', 'sdafdsfdsfsadf', 'sdafdsfdsfsadf', 'sdafdsfdsfsadf'),
(242591, 'sdafdsfdsfsadf', 'sdafdsfdsfsadf', 'sdafdsfdsfsadf', 'sdafdsfdsfsadf'),
(242591, 'sdafdsfdsfsadf', 'sdafdsfdsfsadf', 'sdafdsfdsfsadf', 'sdafdsfdsfsadf'),
(242591, 'vxcvcxvcxv', 'cxvxczvzxcvxczv', 'xcvxczvzxcvxc', 'vcxvxczvxzcvcxvzx');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pruebasevaluacionescomplementarias_cabeza_y_torax`
--

CREATE TABLE `pruebasevaluacionescomplementarias_cabeza_y_torax` (
  `id_ficha` int(11) DEFAULT NULL,
  `pruebas` varchar(255) DEFAULT NULL,
  `resultadosyanalisis` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `pruebasevaluacionescomplementarias_cabeza_y_torax`
--

INSERT INTO `pruebasevaluacionescomplementarias_cabeza_y_torax` (`id_ficha`, `pruebas`, `resultadosyanalisis`) VALUES
(242591, 'Hola', 'Hola'),
(242591, 'sdafdsfdsfsadf', 'sdafdsfdsfsadf'),
(242591, 'sdafdsfdsfsadf', 'sdafdsfdsfsadf'),
(242591, 'sdafdsfdsfsadf', 'sdafdsfdsfsadf');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pruebasevaluacionescomplementarias_miembro_inferior`
--

CREATE TABLE `pruebasevaluacionescomplementarias_miembro_inferior` (
  `id_ficha` int(11) DEFAULT NULL,
  `pruebas` varchar(255) DEFAULT NULL,
  `resultadosyanalisis` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `pruebasevaluacionescomplementarias_miembro_inferior`
--

INSERT INTO `pruebasevaluacionescomplementarias_miembro_inferior` (`id_ficha`, `pruebas`, `resultadosyanalisis`) VALUES
(242591, 'Hola', 'Hola'),
(242591, 'sdafdsfdsfsadf', 'sdafdsfdsfsadf'),
(242591, 'sdafdsfdsfsadf', 'sdafdsfdsfsadf'),
(242591, 'sdafdsfdsfsadf', 'sdafdsfdsfsadf');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pruebasevaluacionescomplementarias_miembro_superior`
--

CREATE TABLE `pruebasevaluacionescomplementarias_miembro_superior` (
  `id_ficha` int(11) DEFAULT NULL,
  `pruebas` varchar(255) DEFAULT NULL,
  `resultadosyanalisis` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `pruebasevaluacionescomplementarias_miembro_superior`
--

INSERT INTO `pruebasevaluacionescomplementarias_miembro_superior` (`id_ficha`, `pruebas`, `resultadosyanalisis`) VALUES
(242591, 'Hola1', 'Hola'),
(242591, 'sdafdsfdsfsadf', 'sdafdsfdsfsadf'),
(242591, 'sdafdsfdsfsadf', 'sdafdsfdsfsadf'),
(242591, 'sdafdsfdsfsadf', 'sdafdsfdsfsadf');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reflejososteotendinosos_miembro_inferior`
--

CREATE TABLE `reflejososteotendinosos_miembro_inferior` (
  `id_ficha` int(11) DEFAULT NULL,
  `izq` varchar(255) DEFAULT NULL,
  `rot` varchar(255) DEFAULT NULL,
  `der` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `reflejososteotendinosos_miembro_inferior`
--

INSERT INTO `reflejososteotendinosos_miembro_inferior` (`id_ficha`, `izq`, `rot`, `der`) VALUES
(242591, 'Hola', 'Rotuliano', 'Hola'),
(242591, 'sdafdsfdsfsadf', 'Aquileo', 'sdafdsfdsfsadf');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reflejososteotendinosos_miembro_superior`
--

CREATE TABLE `reflejososteotendinosos_miembro_superior` (
  `id_ficha` int(11) DEFAULT NULL,
  `izq` varchar(255) DEFAULT NULL,
  `rot` varchar(255) DEFAULT NULL,
  `der` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `reflejososteotendinosos_miembro_superior`
--

INSERT INTO `reflejososteotendinosos_miembro_superior` (`id_ficha`, `izq`, `rot`, `der`) VALUES
(242591, 'Hola', 'Bicipital', 'Hola'),
(242591, 'sdafdsfdsfsadf', 'Tricipital', 'sdafdsfdsfsadf'),
(242591, 'sdafdsfdsfsadf', 'Braquioradial', 'sdafdsfdsfsadf'),
(242591, 'sdafdsfdsfsadf', 'Estiloradial', 'sdafdsfdsfsadf');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rol_asignacion`
--

CREATE TABLE `rol_asignacion` (
  `id` int(11) UNSIGNED NOT NULL,
  `nombre` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `rol_asignacion`
--

INSERT INTO `rol_asignacion` (`id`, `nombre`) VALUES
(1, 'Administrador'),
(2, 'Capturador');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `vistafrontal`
--

CREATE TABLE `vistafrontal` (
  `id_ficha` int(11) DEFAULT NULL,
  `alineacion_corporal` varchar(50) DEFAULT NULL,
  `observaciones` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `vistafrontal`
--

INSERT INTO `vistafrontal` (`id_ficha`, `alineacion_corporal`, `observaciones`) VALUES
(242591, 'Cabeza', 'Hola1'),
(242591, 'Hombros', 'sdafdsfdsfsadf'),
(242591, 'Miembros Superiores', 'sdafdsfdsfsadf'),
(242591, 'Tronco', 'sdafdsfdsfsadf'),
(242591, 'Cadera', 'sdafdsfdsfsadf'),
(242591, 'Rodillas', 'sdafdsfdsfsadf'),
(242591, 'Pies', 'sdafdsfdsfsadf');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `vistalateral`
--

CREATE TABLE `vistalateral` (
  `id_ficha` int(11) DEFAULT NULL,
  `alineacion_corporal` varchar(50) DEFAULT NULL,
  `observaciones` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `vistalateral`
--

INSERT INTO `vistalateral` (`id_ficha`, `alineacion_corporal`, `observaciones`) VALUES
(242591, 'Cabeza', 'Hola1'),
(242591, 'Hombros', 'sdafdsfdsfsadf'),
(242591, 'Miembros Superiores', 'sdafdsfdsfsadf'),
(242591, 'Tronco', 'sdafdsfdsfsadf'),
(242591, 'Cadera', 'sdafdsfdsfsadf'),
(242591, 'Rodillas', 'sdafdsfdsfsadf'),
(242591, 'Pies', 'sdafdsfdsfsadf');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `vistaposterior`
--

CREATE TABLE `vistaposterior` (
  `id_ficha` int(11) DEFAULT NULL,
  `alineacion_corporal` varchar(50) DEFAULT NULL,
  `observaciones` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `vistaposterior`
--

INSERT INTO `vistaposterior` (`id_ficha`, `alineacion_corporal`, `observaciones`) VALUES
(242591, 'Cabeza', 'Hola1'),
(242591, 'Hombros', 'sdafdsfdsfsadf'),
(242591, 'Miembros Superiores', 'sdafdsfdsfsadf'),
(242591, 'Tronco', 'sdafdsfdsfsadf'),
(242591, 'Cadera', 'sdafdsfdsfsadf'),
(242591, 'Rodillas', 'sdafdsfdsfsadf'),
(242591, 'Pies', 'sdafdsfdsfsadf');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `antecedentesheredofamiliares`
--
ALTER TABLE `antecedentesheredofamiliares`
  ADD KEY `id_ficha` (`id_ficha`);

--
-- Indices de la tabla `antecedentespersonalesnopatologicos`
--
ALTER TABLE `antecedentespersonalesnopatologicos`
  ADD KEY `id_ficha` (`id_ficha`);

--
-- Indices de la tabla `antecedentes_ginecobstetricos`
--
ALTER TABLE `antecedentes_ginecobstetricos`
  ADD KEY `id_ficha` (`id_ficha`);

--
-- Indices de la tabla `antecedentes_padecimientoactual`
--
ALTER TABLE `antecedentes_padecimientoactual`
  ADD KEY `id_ficha` (`id_ficha`);

--
-- Indices de la tabla `antecedentes_patologicos`
--
ALTER TABLE `antecedentes_patologicos`
  ADD KEY `id_ficha` (`id_ficha`);

--
-- Indices de la tabla `ciclo_marcha_miembro_inferior`
--
ALTER TABLE `ciclo_marcha_miembro_inferior`
  ADD KEY `id_ficha` (`id_ficha`);

--
-- Indices de la tabla `exploracion`
--
ALTER TABLE `exploracion`
  ADD KEY `id_ficha` (`id_ficha`);

--
-- Indices de la tabla `ficha_identificaciones`
--
ALTER TABLE `ficha_identificaciones`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `fuerza_muscular_cabeza_y_torax`
--
ALTER TABLE `fuerza_muscular_cabeza_y_torax`
  ADD KEY `id_ficha` (`id_ficha`);

--
-- Indices de la tabla `fuerza_muscular_cabeza_y_torax1`
--
ALTER TABLE `fuerza_muscular_cabeza_y_torax1`
  ADD KEY `id_ficha` (`id_ficha`);

--
-- Indices de la tabla `fuerza_muscular_miembro_inferior`
--
ALTER TABLE `fuerza_muscular_miembro_inferior`
  ADD KEY `id_ficha` (`id_ficha`);

--
-- Indices de la tabla `fuerza_muscular_miembro_superior`
--
ALTER TABLE `fuerza_muscular_miembro_superior`
  ADD KEY `id_ficha` (`id_ficha`);

--
-- Indices de la tabla `goniometria_cabeza_y_torax`
--
ALTER TABLE `goniometria_cabeza_y_torax`
  ADD KEY `id_ficha` (`id_ficha`);

--
-- Indices de la tabla `goniometria_miembro_inferior`
--
ALTER TABLE `goniometria_miembro_inferior`
  ADD KEY `id_ficha` (`id_ficha`);

--
-- Indices de la tabla `goniometria_miembro_superior`
--
ALTER TABLE `goniometria_miembro_superior`
  ADD KEY `id_ficha` (`id_ficha`);

--
-- Indices de la tabla `inicio_sesion`
--
ALTER TABLE `inicio_sesion`
  ADD PRIMARY KEY (`id`),
  ADD KEY `rol` (`rol`);

--
-- Indices de la tabla `notas_seguimientos`
--
ALTER TABLE `notas_seguimientos`
  ADD KEY `id_ficha` (`id_ficha`);

--
-- Indices de la tabla `partes_cuerpo`
--
ALTER TABLE `partes_cuerpo`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `partes_cuerpo_cabeza_y_torax`
--
ALTER TABLE `partes_cuerpo_cabeza_y_torax`
  ADD KEY `id_partes` (`id_partes`),
  ADD KEY `id_ficha` (`id_ficha`);

--
-- Indices de la tabla `partes_cuerpo_cabeza_y_torax1`
--
ALTER TABLE `partes_cuerpo_cabeza_y_torax1`
  ADD KEY `id_partes` (`id_partes`),
  ADD KEY `id_ficha` (`id_ficha`);

--
-- Indices de la tabla `partes_cuerpo_miembro_inferior`
--
ALTER TABLE `partes_cuerpo_miembro_inferior`
  ADD KEY `id_partes` (`id_partes`),
  ADD KEY `id_ficha` (`id_ficha`);

--
-- Indices de la tabla `partes_cuerpo_miembro_superior`
--
ALTER TABLE `partes_cuerpo_miembro_superior`
  ADD KEY `id_partes` (`id_partes`),
  ADD KEY `id_ficha` (`id_ficha`);

--
-- Indices de la tabla `plan_tratamientos`
--
ALTER TABLE `plan_tratamientos`
  ADD KEY `id_ficha` (`id_ficha`);

--
-- Indices de la tabla `pruebasevaluacionescomplementarias_cabeza_y_torax`
--
ALTER TABLE `pruebasevaluacionescomplementarias_cabeza_y_torax`
  ADD KEY `id_ficha` (`id_ficha`);

--
-- Indices de la tabla `pruebasevaluacionescomplementarias_miembro_inferior`
--
ALTER TABLE `pruebasevaluacionescomplementarias_miembro_inferior`
  ADD KEY `id_ficha` (`id_ficha`);

--
-- Indices de la tabla `pruebasevaluacionescomplementarias_miembro_superior`
--
ALTER TABLE `pruebasevaluacionescomplementarias_miembro_superior`
  ADD KEY `id_ficha` (`id_ficha`);

--
-- Indices de la tabla `reflejososteotendinosos_miembro_inferior`
--
ALTER TABLE `reflejososteotendinosos_miembro_inferior`
  ADD KEY `id_ficha` (`id_ficha`);

--
-- Indices de la tabla `reflejososteotendinosos_miembro_superior`
--
ALTER TABLE `reflejososteotendinosos_miembro_superior`
  ADD KEY `id_ficha` (`id_ficha`);

--
-- Indices de la tabla `rol_asignacion`
--
ALTER TABLE `rol_asignacion`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `vistafrontal`
--
ALTER TABLE `vistafrontal`
  ADD KEY `id_ficha` (`id_ficha`);

--
-- Indices de la tabla `vistalateral`
--
ALTER TABLE `vistalateral`
  ADD KEY `id_ficha` (`id_ficha`);

--
-- Indices de la tabla `vistaposterior`
--
ALTER TABLE `vistaposterior`
  ADD KEY `id_ficha` (`id_ficha`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `ficha_identificaciones`
--
ALTER TABLE `ficha_identificaciones`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=242592;

--
-- AUTO_INCREMENT de la tabla `inicio_sesion`
--
ALTER TABLE `inicio_sesion`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=47;

--
-- AUTO_INCREMENT de la tabla `partes_cuerpo`
--
ALTER TABLE `partes_cuerpo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `rol_asignacion`
--
ALTER TABLE `rol_asignacion`
  MODIFY `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `antecedentesheredofamiliares`
--
ALTER TABLE `antecedentesheredofamiliares`
  ADD CONSTRAINT `antecedentesheredofamiliares_ibfk_1` FOREIGN KEY (`id_ficha`) REFERENCES `ficha_identificaciones` (`id`);

--
-- Filtros para la tabla `antecedentespersonalesnopatologicos`
--
ALTER TABLE `antecedentespersonalesnopatologicos`
  ADD CONSTRAINT `antecedentespersonalesnopatologicos_ibfk_1` FOREIGN KEY (`id_ficha`) REFERENCES `ficha_identificaciones` (`id`);

--
-- Filtros para la tabla `antecedentes_ginecobstetricos`
--
ALTER TABLE `antecedentes_ginecobstetricos`
  ADD CONSTRAINT `antecedentes_ginecobstetricos_ibfk_1` FOREIGN KEY (`id_ficha`) REFERENCES `ficha_identificaciones` (`id`);

--
-- Filtros para la tabla `antecedentes_padecimientoactual`
--
ALTER TABLE `antecedentes_padecimientoactual`
  ADD CONSTRAINT `antecedentes_padecimientoactual_ibfk_1` FOREIGN KEY (`id_ficha`) REFERENCES `ficha_identificaciones` (`id`);

--
-- Filtros para la tabla `antecedentes_patologicos`
--
ALTER TABLE `antecedentes_patologicos`
  ADD CONSTRAINT `antecedentes_patologicos_ibfk_1` FOREIGN KEY (`id_ficha`) REFERENCES `ficha_identificaciones` (`id`);

--
-- Filtros para la tabla `ciclo_marcha_miembro_inferior`
--
ALTER TABLE `ciclo_marcha_miembro_inferior`
  ADD CONSTRAINT `ciclo_marcha_miembro_inferior_ibfk_1` FOREIGN KEY (`id_ficha`) REFERENCES `ficha_identificaciones` (`id`);

--
-- Filtros para la tabla `exploracion`
--
ALTER TABLE `exploracion`
  ADD CONSTRAINT `exploracion_ibfk_1` FOREIGN KEY (`id_ficha`) REFERENCES `ficha_identificaciones` (`id`);

--
-- Filtros para la tabla `fuerza_muscular_cabeza_y_torax`
--
ALTER TABLE `fuerza_muscular_cabeza_y_torax`
  ADD CONSTRAINT `fuerza_muscular_cabeza_y_torax_ibfk_1` FOREIGN KEY (`id_ficha`) REFERENCES `ficha_identificaciones` (`id`);

--
-- Filtros para la tabla `fuerza_muscular_cabeza_y_torax1`
--
ALTER TABLE `fuerza_muscular_cabeza_y_torax1`
  ADD CONSTRAINT `fuerza_muscular_cabeza_y_torax1_ibfk_1` FOREIGN KEY (`id_ficha`) REFERENCES `ficha_identificaciones` (`id`);

--
-- Filtros para la tabla `fuerza_muscular_miembro_inferior`
--
ALTER TABLE `fuerza_muscular_miembro_inferior`
  ADD CONSTRAINT `fuerza_muscular_miembro_inferior_ibfk_1` FOREIGN KEY (`id_ficha`) REFERENCES `ficha_identificaciones` (`id`);

--
-- Filtros para la tabla `fuerza_muscular_miembro_superior`
--
ALTER TABLE `fuerza_muscular_miembro_superior`
  ADD CONSTRAINT `fuerza_muscular_miembro_superior_ibfk_1` FOREIGN KEY (`id_ficha`) REFERENCES `ficha_identificaciones` (`id`);

--
-- Filtros para la tabla `goniometria_cabeza_y_torax`
--
ALTER TABLE `goniometria_cabeza_y_torax`
  ADD CONSTRAINT `goniometria_cabeza_y_torax_ibfk_1` FOREIGN KEY (`id_ficha`) REFERENCES `ficha_identificaciones` (`id`);

--
-- Filtros para la tabla `goniometria_miembro_inferior`
--
ALTER TABLE `goniometria_miembro_inferior`
  ADD CONSTRAINT `goniometria_miembro_inferior_ibfk_1` FOREIGN KEY (`id_ficha`) REFERENCES `ficha_identificaciones` (`id`);

--
-- Filtros para la tabla `goniometria_miembro_superior`
--
ALTER TABLE `goniometria_miembro_superior`
  ADD CONSTRAINT `goniometria_miembro_superior_ibfk_1` FOREIGN KEY (`id_ficha`) REFERENCES `ficha_identificaciones` (`id`);

--
-- Filtros para la tabla `inicio_sesion`
--
ALTER TABLE `inicio_sesion`
  ADD CONSTRAINT `inicio_sesion_ibfk_1` FOREIGN KEY (`rol`) REFERENCES `rol_asignacion` (`id`);

--
-- Filtros para la tabla `notas_seguimientos`
--
ALTER TABLE `notas_seguimientos`
  ADD CONSTRAINT `notas_seguimientos_ibfk_1` FOREIGN KEY (`id_ficha`) REFERENCES `ficha_identificaciones` (`id`);

--
-- Filtros para la tabla `partes_cuerpo_cabeza_y_torax`
--
ALTER TABLE `partes_cuerpo_cabeza_y_torax`
  ADD CONSTRAINT `partes_cuerpo_cabeza_y_torax_ibfk_1` FOREIGN KEY (`id_partes`) REFERENCES `partes_cuerpo` (`id`),
  ADD CONSTRAINT `partes_cuerpo_cabeza_y_torax_ibfk_2` FOREIGN KEY (`id_ficha`) REFERENCES `ficha_identificaciones` (`id`);

--
-- Filtros para la tabla `partes_cuerpo_cabeza_y_torax1`
--
ALTER TABLE `partes_cuerpo_cabeza_y_torax1`
  ADD CONSTRAINT `partes_cuerpo_cabeza_y_torax1_ibfk_1` FOREIGN KEY (`id_partes`) REFERENCES `partes_cuerpo` (`id`),
  ADD CONSTRAINT `partes_cuerpo_cabeza_y_torax1_ibfk_2` FOREIGN KEY (`id_ficha`) REFERENCES `ficha_identificaciones` (`id`);

--
-- Filtros para la tabla `partes_cuerpo_miembro_inferior`
--
ALTER TABLE `partes_cuerpo_miembro_inferior`
  ADD CONSTRAINT `partes_cuerpo_miembro_inferior_ibfk_1` FOREIGN KEY (`id_partes`) REFERENCES `partes_cuerpo` (`id`),
  ADD CONSTRAINT `partes_cuerpo_miembro_inferior_ibfk_2` FOREIGN KEY (`id_ficha`) REFERENCES `ficha_identificaciones` (`id`);

--
-- Filtros para la tabla `partes_cuerpo_miembro_superior`
--
ALTER TABLE `partes_cuerpo_miembro_superior`
  ADD CONSTRAINT `partes_cuerpo_miembro_superior_ibfk_1` FOREIGN KEY (`id_partes`) REFERENCES `partes_cuerpo` (`id`),
  ADD CONSTRAINT `partes_cuerpo_miembro_superior_ibfk_2` FOREIGN KEY (`id_ficha`) REFERENCES `ficha_identificaciones` (`id`);

--
-- Filtros para la tabla `plan_tratamientos`
--
ALTER TABLE `plan_tratamientos`
  ADD CONSTRAINT `plan_tratamientos_ibfk_1` FOREIGN KEY (`id_ficha`) REFERENCES `ficha_identificaciones` (`id`);

--
-- Filtros para la tabla `pruebasevaluacionescomplementarias_cabeza_y_torax`
--
ALTER TABLE `pruebasevaluacionescomplementarias_cabeza_y_torax`
  ADD CONSTRAINT `pruebasevaluacionescomplementarias_cabeza_y_torax_ibfk_1` FOREIGN KEY (`id_ficha`) REFERENCES `ficha_identificaciones` (`id`);

--
-- Filtros para la tabla `pruebasevaluacionescomplementarias_miembro_inferior`
--
ALTER TABLE `pruebasevaluacionescomplementarias_miembro_inferior`
  ADD CONSTRAINT `pruebasevaluacionescomplementarias_miembro_inferior_ibfk_1` FOREIGN KEY (`id_ficha`) REFERENCES `ficha_identificaciones` (`id`);

--
-- Filtros para la tabla `pruebasevaluacionescomplementarias_miembro_superior`
--
ALTER TABLE `pruebasevaluacionescomplementarias_miembro_superior`
  ADD CONSTRAINT `pruebasevaluacionescomplementarias_miembro_superior_ibfk_1` FOREIGN KEY (`id_ficha`) REFERENCES `ficha_identificaciones` (`id`);

--
-- Filtros para la tabla `reflejososteotendinosos_miembro_inferior`
--
ALTER TABLE `reflejososteotendinosos_miembro_inferior`
  ADD CONSTRAINT `reflejososteotendinosos_miembro_inferior_ibfk_1` FOREIGN KEY (`id_ficha`) REFERENCES `ficha_identificaciones` (`id`);

--
-- Filtros para la tabla `reflejososteotendinosos_miembro_superior`
--
ALTER TABLE `reflejososteotendinosos_miembro_superior`
  ADD CONSTRAINT `reflejososteotendinosos_miembro_superior_ibfk_1` FOREIGN KEY (`id_ficha`) REFERENCES `ficha_identificaciones` (`id`);

--
-- Filtros para la tabla `vistafrontal`
--
ALTER TABLE `vistafrontal`
  ADD CONSTRAINT `vistafrontal_ibfk_1` FOREIGN KEY (`id_ficha`) REFERENCES `ficha_identificaciones` (`id`);

--
-- Filtros para la tabla `vistalateral`
--
ALTER TABLE `vistalateral`
  ADD CONSTRAINT `vistalateral_ibfk_1` FOREIGN KEY (`id_ficha`) REFERENCES `ficha_identificaciones` (`id`);

--
-- Filtros para la tabla `vistaposterior`
--
ALTER TABLE `vistaposterior`
  ADD CONSTRAINT `vistaposterior_ibfk_1` FOREIGN KEY (`id_ficha`) REFERENCES `ficha_identificaciones` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
