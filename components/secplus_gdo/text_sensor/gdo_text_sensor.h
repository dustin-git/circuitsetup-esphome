#pragma once

#include "esphome/components/text_sensor/text_sensor.h"
#include "esphome/core/component.h" 

namespace esphome {
namespace secplus_gdo {

enum TextSensorType : uint8_t {
  DEVICE_TYPE,
  MANUFACTURER,
};

class GDOTextSensor : public text_sensor::TextSensor, public Component {
 public:
  GDOTextSensor() = default;

  void set_sync_state(bool synced) { this->publish_state(synced ? "Synced" : "Not Synced"); }
  void set_component_source(const std::string &source) { this->component_source_ = source; }
  void set_type(TextSensorType type) { this->type_ = type; }
  TextSensorType get_type() const { return this->type_; }

 protected:
  TextSensorType type_;
  std::string component_source_;
};

}  // namespace secplus_gdo
}  // namespace esphome
