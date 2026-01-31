import { Column, Entity, PrimaryGeneratedColumn } from 'typeorm'

@Entity()
export class Build {
  @PrimaryGeneratedColumn()
  id: number

  @Column()
  ownerAddress: string

  @Column({ type: 'timestamp', default: () => 'CURRENT_TIMESTAMP' })
  createdAt: Date
}