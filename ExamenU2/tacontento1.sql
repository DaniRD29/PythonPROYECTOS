-- volcado SQL phpMyAdmin
-- versión 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 03-04-2023 a las 12:31:02
-- Versión del servidor: 10.4.27-MariaDB
-- Versión de PHP: 8.2.0

PONER SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
INICIAR TRANSACCIÓN;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 NOMBRES DE CONJUNTO UTF8MB4 */;

--
-- Base de datos: 'tacontento1'
--
CREAR BASE DE DATOS SI NO EXISTE 'tacontento1' JUEGO DE CARACTERES PREDETERMINADO utf8mb4 COLLATE utf8mb4_general_ci;
USE 'tacontento1';

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla 'pedidos'
--

CREATE TABLE 'pedidos` (
  'id' int(40) NOT NULL,
  'user' varchar(35) NOT NULL,
  'contra' varchar(35) NO NULO
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla 'pedidos'
--
ALTER TABLE 'pedidos'
 AGREGAR CLAVE PRINCIPAL ('id');

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla 'pedidos'
--
ALTER TABLE 'pedidos'
 MODIFY 'id' int(40) NOT NULL AUTO_INCREMENT;
COMETER;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;