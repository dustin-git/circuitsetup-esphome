import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import text_sensor
from esphome.const import CONF_ID

from .. import SECPLUS_GDO_CONFIG_SCHEMA, secplus_gdo_ns, CONF_SECPLUS_GDO_ID

DEPENDENCIES = ["secplus_gdo"]

GDOTextSensor = secplus_gdo_ns.class_("GDOTextSensor", text_sensor.TextSensor, cg.Component)

CONF_TYPE = "type"

TYPES = {
    "device_type": "register_device_type",
    "manufacturer": "register_manufacturer",
}

CONFIG_SCHEMA = (
    text_sensor.text_sensor_schema(GDOTextSensor)
    .extend({
        cv.Required(CONF_TYPE): cv.enum(TYPES, lower=True),
    })
    .extend(SECPLUS_GDO_CONFIG_SCHEMA)
)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await text_sensor.register_text_sensor(var, config)
    await cg.register_component(var, config)
    parent = await cg.get_variable(config[CONF_SECPLUS_GDO_ID])
    fcall = str(parent) + "->" + str(TYPES[config[CONF_TYPE]])
    text = fcall + "(" + str(var) + ")"
    cg.add(cg.RawExpression(text))
    text = "secplus_gdo::TextSensorType::" + str(config[CONF_TYPE]).upper()
    cg.add(var.set_type(cg.RawExpression(text)))
