-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 25-10-2024 a las 21:49:38
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
(48440, 'Cáncer', 0, 1, 'sdfsdfsdfdsf', 1, 0, 'sdfsdfsdfdsf', 'sdfsdfsdfdsf'),
(48440, 'Diabetes', 1, 0, 'sdfsdfsdfdsf', 0, 1, 'sdfsdfsdfdsf', 'sdfsdfsdfdsf'),
(48440, 'Hipertensión', 0, 1, 'sdfsdfsdfdsf', 1, 0, 'sdfsdfsdfdsf', 'sdfsdfsdfdsf'),
(48440, 'Enfermedades Cardiacas', 1, 0, 'sdfsdfsdfdsf', 0, 1, 'sdfsdfsdfdsf', 'sdfsdfsdfdsf'),
(48440, 'Enfermedades Mentales', 0, 1, 'sdfsdfsdfdsf', 1, 0, 'sdfsdfsdfdsf', 'sdfsdfsdfdsf'),
(48440, 'Alergias', 1, 0, 'sdfsdfsdfdsf', 0, 1, 'sdfsdfsdfdsf', 'sdfsdfsdfdsf');

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
(48440, 'sdfsdfsdfdsf', 'sdfsdfsdfdsf', 'sdfsdfsdfdsf', 'sdfsdfsdfdsf', 'sdfsdfsdfdsf', 'sdfsdfsdfdsf', 'sdfsdfsdfdsf', 3, 3.9, 'sdfsdfsdfdsf', 'sdfsdfsdfdsf', 'sdfsdfsdfdsf', 6, '6', 'sdfsdfsdfdsf', 'sdfsdfsdfdsf', 'sdfsdfsdfdsf', 'sdfsdfsdfdsf');

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
(48440, 'sdfsdfsdfdsf', '2024-10-02', 'sdfsdfsdfdsf', '2024-09-25', 'sdfsdfsdfdsf', 1, 1, 1, 'sdfsdfsdfdsf');

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
(48440, 'sdfsdfsdfdsf');

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
(48440, 'Traumatismos', 0, 1, 34, 'sdfsdfsdfdsf', 'sdfsdfsdfdsf', 'sdfsdfsdfdsf'),
(48440, 'Cirugías', 1, 0, 34, 'sdfsdfsdfdsf', 'sdfsdfsdfdsf', 'sdfsdfsdfdsf'),
(48440, 'Luxaciones', 0, 1, 34, 'sdfsdfsdfdsf', 'sdfsdfsdfdsf', 'sdfsdfsdfdsf'),
(48440, 'Alergias', 1, 0, 34, 'sdfsdfsdfdsf', 'sdfsdfsdfdsf', 'sdfsdfsdfdsf'),
(48440, 'Toxicomanías', 0, 1, 34, 'sdfsdfsdfdsf', 'sdfsdfsdfdsf', 'sdfsdfsdfdsf'),
(48440, 'Padecimientos psiquiátricos', 1, 0, 34, 'sdfsdfsdfdsf', 'sdfsdfsdfdsf', 'sdfsdfsdfdsf');

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
(48440, 'sdfsdfsdfdsf', 'sdfsdfsdfdsf', 'sdfsdfsdfdsf', 'sdfsdfsdfdsf', 'sdfsdfsdfdsf', 'sdfsdfsdfdsf', 'sdfsdfsdfdsf', 'sdfsdfsdfdsf', 'sdfsdfsdfdsf', 'sdfsdfsdfdsf', 'sdfsdfsdfdsf', 'sdfsdfsdfdsf', 'sdfsdfsdfdsf', 'sdfsdfsdfdsf', 'sdfsdfsdfdsf', 'sdfsdfsdfdsf', 'sdfsdfsdfdsf', 'sdfsdfsdfdsf', 'sdfsdfsdfdsf', 'sdfsdfsdfdsf', 'sdfsdfsdfdsf', 'sdfsdfsdfdsf', 'sdfsdfsdfdsf');

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
(48440, 'sdfsdfsdfdsf', 4.80, 6.90, 3.80, 4.90, 6, 5, '5', 3.60, 'sdfsdfsdfdsf', 'sdfsdfsdfdsf');

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
(48440, '2024-10-25', 'sdfsdfsdfdsf', 'femenino', 4454, 34, '2024-10-09', 'sdfsdfsdfdsf', 'sdfsdfsdfdsf', 'sdfsdfsdfdsf', 'soltero', 'sdfsdfsdfdsf', '8899776655', 'sdfsdfsdfdsf', '5566778899', 'sdfsdfsdfdsf', 'sdfsdfsdfdsf', 'sdfsdfsdfdsf');

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
(48440, 'Extensión de cabeza', 'sdfsdfsdfdsf'),
(48440, 'Extensión de cuello', 'sdfsdfsdfdsf'),
(48440, 'Extensión conjunta', 'sdfsdfsdfdsf'),
(48440, 'Flexión de cabeza', 'sdfsdfsdfdsf'),
(48440, 'Flexión de cuello', 'sdfsdfsdfdsf'),
(48440, 'Flexión conjunta', 'sdfsdfsdfdsf'),
(48440, 'Flexión y rotación conjuntas', 'sdfsdfsdfdsf'),
(48440, 'Rotación del cuello', 'sdfsdfsdfdsf'),
(48440, 'Observaciones', 'sdfsdfsdfdsf');

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
(48440, 'Extensión lumbar', 'sdfsdfsdfdsf'),
(48440, 'Extensión torácica', 'sdfsdfsdfdsf'),
(48440, 'Elevación pélvica', 'sdfsdfsdfdsf'),
(48440, 'Flexión', 'sdfsdfsdfdsf'),
(48440, 'Rotación', 'sdfsdfsdfdsf'),
(48440, 'Inspiración', 'sdfsdfsdfdsf'),
(48440, 'Espiración forzada indirecta', 'sdfsdfsdfdsf');

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
(48440, 'sdfsdfsdfdsf', 'Flexión de cadera', 'sdfsdfsdfdsf'),
(48440, 'sdfsdfsdfdsf', 'Extensión de la cadera', 'sdfsdfsdfdsf'),
(48440, 'sdfsdfsdfdsf', 'Abducción de la cadera', 'sdfsdfsdfdsf'),
(48440, 'sdfsdfsdfdsf', 'Aducción de la cadera', 'sdfsdfsdfdsf'),
(48440, 'sdfsdfsdfdsf', 'Rotación externa de la cadera', 'sdfsdfsdfdsf'),
(48440, 'sdfsdfsdfdsf', 'Rotación interna de la cadera', 'sdfsdfsdfdsf'),
(48440, 'sdfsdfsdfdsf', 'Flexión de la rodilla', 'sdfsdfsdfdsf'),
(48440, 'sdfsdfsdfdsf', 'Extensión de la rodilla', 'sdfsdfsdfdsf'),
(48440, 'sdfsdfsdfdsf', 'Flexión plantar del tobillo', 'sdfsdfsdfdsf'),
(48440, 'sdfsdfsdfdsf', 'Dorsiflexión e inversión del pie', 'sdfsdfsdfdsf'),
(48440, 'sdfsdfsdfdsf', 'Inversión del pie', 'sdfsdfsdfdsf'),
(48440, 'sdfsdfsdfdsf', 'Eversión del pie con flexión plantar', 'sdfsdfsdfdsf'),
(48440, 'sdfsdfsdfdsf', 'Eversión del pie con dorsiflexión', 'sdfsdfsdfdsf');

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
(48440, 'sdfsdfsdfdsf', 'Abducción y rotación superior de la escápula', 'sdfsdfsdfdsf'),
(48440, 'sdfsdfsdfdsf', 'Elevación de la escápula', 'sdfsdfsdfdsf'),
(48440, 'sdfsdfsdfdsf', 'Aducción de la escápula', 'sdfsdfsdfdsf'),
(48440, 'sdfsdfsdfdsf', 'Aducción y descenso escapular', 'sdfsdfsdfdsf'),
(48440, 'sdfsdfsdfdsf', 'Aducción y rotación inferior de la escápula', 'sdfsdfsdfdsf'),
(48440, 'sdfsdfsdfdsf', 'Flexión del hombro', 'sdfsdfsdfdsf'),
(48440, 'sdfsdfsdfdsf', 'Extensión de hombro', 'sdfsdfsdfdsf'),
(48440, 'sdfsdfsdfdsf', 'Abducción del hombro', 'sdfsdfsdfdsf'),
(48440, 'sdfsdfsdfdsf', 'Abducción horizontal del hombro', 'sdfsdfsdfdsf'),
(48440, 'sdfsdfsdfdsf', 'Aducción horizontal del hombro', 'sdfsdfsdfdsf'),
(48440, 'sdfsdfsdfdsf', 'Rotación externa del hombro', 'sdfsdfsdfdsf'),
(48440, 'sdfsdfsdfdsf', 'Rotación interna del hombro', 'sdfsdfsdfdsf'),
(48440, 'sdfsdfsdfdsf', 'Flexión de codo', 'sdfsdfsdfdsf'),
(48440, 'sdfsdfsdfdsf', 'Extensión de codo', 'sdfsdfsdfdsf'),
(48440, 'sdfsdfsdfdsf', 'Supinación del antebrazo', 'sdfsdfsdfdsf'),
(48440, 'sdfsdfsdfdsf', 'Pronación del antebrazo', 'sdfsdfsdfdsf'),
(48440, 'sdfsdfsdfdsf', 'Flexión de la muñeca', 'sdfsdfsdfdsf'),
(48440, 'sdfsdfsdfdsf', 'Extensión de la muñeca', 'sdfsdfsdfdsf');

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
(48440, '0-35°/45°', 'Flexión', 'sdfsdfsdfdsf'),
(48440, '0-35°/45°', 'Extensión', 'sdfsdfsdfdsf'),
(48440, '0°-45°', 'Inclinación lateral derecha', 'sdfsdfsdfdsf'),
(48440, '0°-45°', 'Inclinación lateral izquierda', 'sdfsdfsdfdsf'),
(48440, '0-60°/80°', 'Rotación derecha', 'sdfsdfsdfdsf'),
(48440, '0-60°/80°', 'Rotación izquierda', 'sdfsdfsdfdsf'),
(48440, '*método de Schober', 'Flexión', 'sdfsdfsdfdsf'),
(48440, '0-30°', 'Extensión', 'sdfsdfsdfdsf'),
(48440, '0-30°/40°', 'Inclinación lateral derecha', 'sdfsdfsdfdsf'),
(48440, '0°-30°/40°', 'Inclinación lateral izquierda', 'sdfsdfsdfdsf'),
(48440, '0-30°', 'Rotación derecha', 'sdfsdfsdfdsf'),
(48440, '0-30°', 'Rotación izquierda', 'sdfsdfsdfdsf');

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
(48440, '0°-140°', 'sdfsdfsdfdsf', 'Flexión de cadera', 'sdfsdfsdfdsf'),
(48440, '0°-10°', 'sdfsdfsdfdsf', 'Extensión de cadera', 'sdfsdfsdfdsf'),
(48440, '0°-50°', 'sdfsdfsdfdsf', 'Abducción de cadera', 'sdfsdfsdfdsf'),
(48440, '0°-30°', 'sdfsdfsdfdsf', 'Aducción de cadera', 'sdfsdfsdfdsf'),
(48440, '0°-50°', 'sdfsdfsdfdsf', 'Rotación externa de cadera', 'sdfsdfsdfdsf'),
(48440, '0°-40°', 'sdfsdfsdfdsf', 'Rotación interna de cadera', 'sdfsdfsdfdsf'),
(48440, '0°-150°', 'sdfsdfsdfdsf', 'Flexión de rodilla', 'sdfsdfsdfdsf'),
(48440, '0°(activa)-10°(pasiva)', 'sdfsdfsdfdsf', 'Extensión de rodilla', 'sdfsdfsdfdsf'),
(48440, '0°-50°', 'sdfsdfsdfdsf', 'Plantiflexión', 'sdfsdfsdfdsf'),
(48440, '0°-30°', 'sdfsdfsdfdsf', 'Dorsiflexión', 'sdfsdfsdfdsf'),
(48440, '0°-60°', 'sdfsdfsdfdsf', 'Inversión del pie', 'sdfsdfsdfdsf'),
(48440, '0°-30°', 'sdfsdfsdfdsf', 'Eversión del pie', 'sdfsdfsdfdsf');

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
(48440, '0°-150°/170°', 'sdfsdfsdfdsf', 'Flexión de hombro', 'sdfsdfsdfdsf'),
(48440, '0°-40°', 'sdfsdfsdfdsf', 'Extensión de hombro', 'sdfsdfsdfdsf'),
(48440, '0-160°/180°', 'sdfsdfsdfdsf', 'Abducción de hombro', 'sdfsdfsdfdsf'),
(48440, '0°-30°', 'sdfsdfsdfdsf', 'Aducción de hombro', 'sdfsdfsdfdsf'),
(48440, '0°-70°', 'sdfsdfsdfdsf', 'Rotación externa de hombro', 'sdfsdfsdfdsf'),
(48440, '0°-70°', 'sdfsdfsdfdsf', 'Rotación interna de hombro', 'sdfsdfsdfdsf'),
(48440, '0°-150°', 'sdfsdfsdfdsf', 'Flexión de codo', 'sdfsdfsdfdsf'),
(48440, '0°(activa)-10°(pasiva)', 'sdfsdfsdfdsf', 'Extensión de codo', 'sdfsdfsdfdsf'),
(48440, '0°-90°', 'sdfsdfsdfdsf', 'Supinación del antebrazo', 'sdfsdfsdfdsf'),
(48440, '0°-90°', 'sdfsdfsdfdsf', 'Pronación del antebrazo', 'sdfsdfsdfdsf'),
(48440, '0°-25°-30°', 'sdfsdfsdfdsf', 'Desviación radial de muñeca', 'sdfsdfsdfdsf'),
(48440, '0°-30°-40°', 'sdfsdfsdfdsf', 'Desviación cubital de la muñeca', 'sdfsdfsdfdsf'),
(48440, '0°-50°/60°', 'sdfsdfsdfdsf', 'Flexión de muñeca', 'sdfsdfsdfdsf'),
(48440, '0°-35°/60°', 'sdfsdfsdfdsf', 'Extensión de muñeca', 'sdfsdfsdfdsf');

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
(37, 'adam.jensen7274@gmail.com', 'scrypt:32768:8:1$2rtqhf0WhdQfzFN4$81927f0aaf49c414886dd6f22d65f81a0f40826a8bd8d450f6dcd796973f3b0430e00b98b8d1e4616e52e0481e1a2aa8ff0a7f92c29e061eeb9f3105f05652fe', 2);

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
(48440, 'sdfsdfsdfdsf', 'sdfsdfsdfdsf', '6345', '2024-10-25', 5, 'sdfsdfsdfdsf', 'sdfsdfsdfdsf', 'sdfsdfsdfdsf');

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
(48440, 3, 'sdfsdfsdfdsf', 'sdfsdfsdfdsf', 'sdfsdfsdfdsf', 4);

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
(48440, 4, 'sdfsdfsdfdsf', 'sdfsdfsdfdsf', 'sdfsdfsdfdsf', 4);

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
(48440, 2, 'sdfsdfsdfdsf', 'sdfsdfsdfdsf', 'sdfsdfsdfdsf', 3);

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
(48440, 1, 'sdfsdfsdfdsf', 'sdfsdfsdfdsf', 'sdfsdfsdfdsf', 5);

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
(48440, 'sdfsdfsdfdsf', 'sdfsdfsdfdsf', 'sdfsdfsdfdsf', 'sdfsdfsdfdsf'),
(48440, 'sdfsdfsdfdsf', 'sdfsdfsdfdsf', 'sdfsdfsdfdsf', 'sdfsdfsdfdsf'),
(48440, 'sdfsdfsdfdsf', 'sdfsdfsdfdsf', 'sdfsdfsdfdsf', 'sdfsdfsdfdsf'),
(48440, 'sdfsdfsdfdsf', 'sdfsdfsdfdsf', 'sdfsdfsdfdsf', 'sdfsdfsdfdsf');

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
(48440, 'sdfsdfsdfdsf', 'sdfsdfsdfdsf'),
(48440, 'sdfsdfsdfdsf', 'sdfsdfsdfdsf'),
(48440, 'sdfsdfsdfdsf', 'sdfsdfsdfdsf'),
(48440, 'sdfsdfsdfdsf', 'sdfsdfsdfdsf');

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
(48440, 'sdfsdfsdfdsf', 'sdfsdfsdfdsf'),
(48440, 'sdfsdfsdfdsf', 'sdfsdfsdfdsf'),
(48440, 'sdfsdfsdfdsf', 'sdfsdfsdfdsf'),
(48440, 'sdfsdfsdfdsf', 'sdfsdfsdfdsf');

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
(48440, 'sdfsdfsdfdsf', 'sdfsdfsdfdsf'),
(48440, 'sdfsdfsdfdsf', 'sdfsdfsdfdsf'),
(48440, 'sdfsdfsdfdsf', 'sdfsdfsdfdsf'),
(48440, 'sdfsdfsdfdsf', 'sdfsdfsdfdsf');

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
(48440, 'sdfsdfsdfdsf', 'Rotuliano', 'sdfsdfsdfdsf'),
(48440, 'sdfsdfsdfdsf', 'Aquileo', 'sdfsdfsdfdsf');

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
(48440, 'sdfsdfsdfdsf', 'Bicipital', 'sdfsdfsdfdsf'),
(48440, 'sdfsdfsdfdsf', 'Tricipital', 'sdfsdfsdfdsf'),
(48440, 'sdfsdfsdfdsf', 'Braquioradial', 'sdfsdfsdfdsf'),
(48440, 'sdfsdfsdfdsf', 'Estiloradial', 'sdfsdfsdfdsf');

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
(48440, 'Cabeza', 'sdfsdfsdfdsf'),
(48440, 'Hombros', 'sdfsdfsdfdsf'),
(48440, 'Miembros Superiores', 'sdfsdfsdfdsf'),
(48440, 'Tronco', 'sdfsdfsdfdsf'),
(48440, 'Cadera', 'sdfsdfsdfdsf'),
(48440, 'Rodillas', 'sdfsdfsdfdsf'),
(48440, 'Pies', 'sdfsdfsdfdsf');

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
(48440, 'Cabeza', 'sdfsdfsdfdsf'),
(48440, 'Hombros', 'sdfsdfsdfdsf'),
(48440, 'Miembros Superiores', 'sdfsdfsdfdsf'),
(48440, 'Tronco', 'sdfsdfsdfdsf'),
(48440, 'Cadera', 'sdfsdfsdfdsf'),
(48440, 'Rodillas', 'sdfsdfsdfdsf'),
(48440, 'Pies', 'sdfsdfsdfdsf');

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
(48440, 'Cabeza', 'sdfsdfsdfdsf'),
(48440, 'Hombros', 'sdfsdfsdfdsf'),
(48440, 'Miembros Superiores', 'sdfsdfsdfdsf'),
(48440, 'Tronco', 'sdfsdfsdfdsf'),
(48440, 'Cadera', 'sdfsdfsdfdsf'),
(48440, 'Rodillas', 'sdfsdfsdfdsf'),
(48440, 'Pies', 'sdfsdfsdfdsf');

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=48441;

--
-- AUTO_INCREMENT de la tabla `inicio_sesion`
--
ALTER TABLE `inicio_sesion`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

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
