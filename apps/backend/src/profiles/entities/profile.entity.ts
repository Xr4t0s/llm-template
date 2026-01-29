// src/profiles/entities/profile.entity.ts
import { Column, Entity, PrimaryGeneratedColumn } from 'typeorm'

@Entity()
export class Profile {
  @PrimaryGeneratedColumn()
  id: number

  @Column({ unique: true })
  address: string

  @Column({ default: 0 })
  builds: number

  @Column({ default: false })
  running: boolean

  @Column({ type: 'int', default: 0 })
  step: number

  @Column({ type: 'int', default: 0 })
  substep: number
}
